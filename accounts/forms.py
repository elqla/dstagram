from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields



class CustomUserChangeForm(UserChangeForm):
    profile_picture = forms.ImageField(label='프로필 사진 바꾸기')
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('username', 'profile_picture',) #'__all__' 

# 
