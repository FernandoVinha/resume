from django.conf import settings
from django.conf.urls.static import static
from django.db import models

TYPE = (('0','public'),('1','private'))

Status = (('To Do','To Do'),('Working','Working'),('Done','Done'))

class Task (models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    link  = models.URLField(null=True, blank=True)
    status = models.CharField(max_length=10,choices=Status)
    def __str__(self):
        return self.title

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    baner = models.ImageField(upload_to= 'apps/static/assets/img/temp/')
    TYPE = models.CharField(max_length=10,choices=TYPE)
    task = models.ManyToManyField(Task)
    description2 = models.TextField()
    progress = models.IntegerField(default=0,null=True, blank=True)
    required_value = models.FloatField(null=True, blank=True)
    amount_donated = models.FloatField(null=True, blank=True)
    biticon_request = models.CharField(max_length=500,null=True, blank=True)
    def image_link(self):
        link = str(self.baner).replace('apps','')
        return(link)
    def donation_progress(self):
        progress = (self.amount_donated*100)/self.required_value
        progress = round(progress,2)
        return(progress)

    def __str__(self):
        return self.name

