# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
from django.urls import path, include
urlpatterns = [
    path('social-auth/', include('social_django.urls', namespace='social')),
 
    # The home page
    path('home', views.index, name='home'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
