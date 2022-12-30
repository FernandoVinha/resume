from django.db import models
from users.models import *

# Create your models here.

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user
    

class Posts(models.Model):
    header = models.TextField(null=True, blank=True)
    footer = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to= 'apps/static/assets/img/temp/',null=True, blank=True)
    code = models.TextField(null=True, blank=True)
    video = models.URLField(null=True, blank=True)
    

    def image_link(self):
        link = str(self.image).replace('apps','')
        return(link)

    def __str__(self):
        return self.header

class Blog(models.Model):
    name = models.CharField(max_length=255)
    baner = models.ImageField(upload_to= 'apps/static/assets/img/temp/',null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    video = models.URLField(null=True, blank=True)
    message = models.ManyToManyField(Message,blank=True)
    posts = models.ManyToManyField(Posts,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def image_link(self):
        link = str(self.baner).replace('apps','')
        return(link)

    def __str__(self):
        return self.name

class Category(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to= 'apps/static/assets/img/temp/',null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    blog = models.ManyToManyField(Blog,blank=True)

    def image_link(self):
        link = str(self.image).replace('apps','')
        return(link)
    def __str__(self):
        return self.title