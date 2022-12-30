from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.template import loader
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from .forms import *
from datetime import datetime, timedelta
from datetime import date
from django.shortcuts import render, get_object_or_404, redirect

from django.db.models import Sum
# Create your views here.
last_month = datetime.today() - timedelta(days=30)

def project(request):

    projects = Project.objects.all()
    context = {'segment': 'project','projects':projects}
    html_template = loader.get_template('project/project.html')
    return HttpResponse(html_template.render(context, request))

def projectView (request,id):
    project = get_object_or_404(Project, pk=id)
    context = {'segment': 'project','project':project}
    

    return render(request, 'project/detail.html',{'context':context})

