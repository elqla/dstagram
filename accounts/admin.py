from django.contrib import admin
from django.contrib.auth.admin import UserAdmin  ###UserAdmin ?
from .models import User

admin.site.register(User, UserAdmin)

