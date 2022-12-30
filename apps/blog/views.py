from django.shortcuts import render
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


def category(request):
    category = Category.objects.all()
    context = {'segment': 'blog','category':category}
    html_template = loader.get_template('blog/category.html')
    return HttpResponse(html_template.render(context, request))

def category_(request,id):
    category = get_object_or_404(Category, pk=id)
    context = {'segment': 'blog','category':category}
    return render(request, 'blog/categoryd.html',{'context':context})

def blog(request,id):

    blog = get_object_or_404(Blog, pk=id)
    context = {'segment': 'blog','blog':blog}
    return render(request, 'blog/blog.html',{'context':context})