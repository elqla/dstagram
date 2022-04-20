from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
###UserAdmin list display 위함..
from .models import User

admin.site.register(User, UserAdmin)

