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
    map = folium.Map(location= [-22.40,-47.57], zoom_start= 1.8, min_zoom =1.8,max_zoom = 18,)
    szt = plugins.ScrollZoomToggler()
    map.add_child(szt)

    for experiences_map in experiences_map:
        if experiences_map.experience == 'study':
            icone= 'glyphicon glyphicon-book'
        if experiences_map.experience == 'job':
            icone= 'glyphicon glyphicon-briefcase'
        if experiences_map.experience == 'life_experience':
            icone = 'glyphicon glyphicon-plane'
        folium.Marker(location=[experiences_map.lat, experiences_map.lon],popup=experiences_map.name,
        icon=folium.Icon(color=experiences_map.color ,icon=icone),).add_to(map)
    map = map._repr_html_()

    context = {'m':map ,'segment': 'Resume','profile':profile,'project':project,'experiences':experiences}

    html_template = loader.get_template('curriculum/curriculum.html')
    return HttpResponse(html_template.render(context, request))


def relatorio_users(request):
    users =  User.objects.all()
    meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
    teste = 1
    data = []
    labels = []
    mes = datetime.now().month + 1
    ano = datetime.now().year
    dia = datetime.now().day +1
    for i in range(12): 
        mes -= 1
        if mes == 0:
            mes = 12
            ano -= 1
        if mes >12:
            mes = 1
            ano = +1
        users_last_month =  User.objects.filter(date_joined__lte = date(ano, mes, dia ))
        y = len(users_last_month)
        labels.append(meses[mes-1])
        data.append(y)
    data_json = {'labels': labels[::-1],'data':data[::-1]}
     
    return JsonResponse(data_json)