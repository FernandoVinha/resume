from django.urls import path, re_path
from apps.project import views
from django.urls import path, include
urlpatterns = [
 
    # The home page
    path('project', views.project, name='project'),
    path('project/<int:id>', views.projectView, name='projectView'),
]
