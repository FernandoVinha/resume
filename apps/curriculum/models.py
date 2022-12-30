from django.db import models
from django.contrib.auth.models import User
# Create your models here.


COLOR = (('lightgray', 'lightgray'), ('pink','pink'), ('darkred','darkred'),
    ('red','red'), ('lightblue','lightblue'), ('darkblue','darkblue'),
    ('darkpurple','darkpurple'), ('green','green'), ('blue','blue'), 
    ('lightgreen','lightgreen'), ('lightred','lightred'), ('gray','gray'),
    ('cadetblue','cadetblue'), ('orange','orange'), ('purple','purple'),
    ('darkgreen','darkgreen'), ('black','black'), ('beige','beige'), ('white','white'))
ICO = (('glyphicon glyphicon-book','glyphicon glyphicon-book'),
    ('glyphicon glyphicon-briefcase','glyphicon glyphicon-briefcase'),
    ('glyphicon glyphicon-plane','glyphicon glyphicon-plane'))
ICOE =(('book','book'),('business_center','business_center'),('flight','flight'))

EXPERIENCE = (('study','study'),('job','job'),('life_experience','life_experience'))




class Experiences(models.Model):
    name = models.CharField(max_length=255)
    lat = models.FloatField()
    lon = models.FloatField()
    color = models.CharField(max_length=40,choices=COLOR,)
    experience = models.CharField(max_length=255,choices=EXPERIENCE)
    start_date =  models.DateField(null = True)
    end_date =  models.DateField(null = True)
    details = models.TextField(null = True)
    def save(self, *args, **kwargs):
        if self.experience == 'study':
            icone= 'book'
        if self.experience == 'job':
            icone= 'business_center'
        if self.experience == 'life_experience':
            icone = 'flight'
        super(Experiences, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    

