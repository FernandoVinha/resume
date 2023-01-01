from django.urls import path, re_path
from apps.curriculum import views
from django.urls import path, include
urlpatterns = [
 
    # The home page
    path('', views.curriculum, name='curriculum'),
]
