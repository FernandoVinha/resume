from django.contrib.auth.models import AbstractUser
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return str(self.name)

class Social(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField()
    icone = models.CharField(max_length=255,help_text = "look for the icons on the website: https://fontawesome.com/v5/icons/github?s=solid&f=brands , Example of use: fab fa-github fa-lg")

    def __str__(self):
        return self.name
        
class User(AbstractUser):
    profession = models.CharField(max_length=255,null = True,blank=True)
    avatar =  models.ImageField(upload_to= 'apps/static/assets/img/temp/',null = True,blank=True)
    background = models.ImageField(upload_to= 'apps/static/assets/img/temp/',null = True,blank=True)
    profile_information = models.TextField(null = True,blank=True)
    location = models.CharField(max_length=255,null = True,blank=True)
    mobile = models.CharField(max_length=255,null = True,blank=True)
    social  = models.ManyToManyField(Social)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING,null = True,blank=True)
    def avatar_link(self):
        link = str(self.avatar).replace('apps/','')
        return(link)

    def background_link(self):
        link = str(self.background).replace('apps/','')
        return(link)