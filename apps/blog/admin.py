from django.contrib import admin


from .models import *
admin.site.register(Message)

admin.site.register(Posts)

admin.site.register(Blog)

admin.site.register(Category)
