# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from apps.blog import views

urlpatterns = [

    path('blog/category', views.category, name='category'),
    path('blog/category/<int:id>', views.category_, name='category_View'),
    path('blog/<int:id>', views.blog, name='blog'),
]
