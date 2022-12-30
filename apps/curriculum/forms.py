from django import forms

from .models import *
from users.models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('__all__')

class ExperiencesForm(forms.ModelForm):
    class Meta:
        model = Experiences
        fields = ('__all__')



class SocialForm(forms.ModelForm):
    class Meta:
        model = Social
        fields = ('__all__')