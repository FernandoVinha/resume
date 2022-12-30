from django import forms

from .models import *
from users.models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('__all__')

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('__all__')

class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('__all__')

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('__all__')

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('__all__')

