from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .forms import UserChangeForm, UserCreationForm
from .models import *



admin.site.register(User)

admin.site.register(Company)

admin.site.register(Social)