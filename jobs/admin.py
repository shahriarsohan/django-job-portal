from django.contrib import admin

# Register your models here.
from .models import Profile, Jobs

admin.site.register(Profile)
admin.site.register(Jobs)
