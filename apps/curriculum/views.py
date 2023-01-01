from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.template import loader
from django.urls import reverse
from folium import plugins
import  folium
from django.contrib.auth.models import *
from django.core.paginator import Paginator
from .forms import *
from ..project.forms import *
from ..blog.forms import *
from datetime import datetime, timedelta
from datetime import date

from django.db.models import Sum
# Create your views here.
last_month = datetime.today() - timedelta(days=30)

def curriculum(request):
    project = Project.objects.all()[:4]
    experiences_map = Experiences.objects.all()
    experiences = Experiences.objects.all().order_by('-end_date')[:10]
    profile =  User.objects.filter(is_superuser=True)
    map = folium.Map(location= [0,-20], zoom_start= 3.2, min_zoom =1.8,max_zoom = 18,)
    szt = plugins.ScrollZoomToggler()
    map.add_child(szt)
    blog = Blog.objects.all()[:6]
    for experiences_map in experiences_map:               
        if experiences_map.experience == 'study':
            icone= 'glyphicon glyphicon-book'
        if experiences_map.experience == 'job':
            icone= 'glyphicon glyphicon-briefcase'
        if experiences_map.experience == 'life_experience':
            icone = 'glyphicon glyphicon-plane'
        folium.Marker(location=[experiences_map.lat, experiences_map.lon],popup=experiences_map.name+"<br>"+experiences_map.details,
        icon=folium.Icon(color=experiences_map.color ,icon=icone),).add_to(map)
    map = map._repr_html_()

    context = {'m':map ,'segment': 'Resume','profile':profile,'project':project,'experiences':experiences,'blog':blog}

    html_template = loader.get_template('curriculum/curriculum.html')
    return HttpResponse(html_template.render(context, request))
