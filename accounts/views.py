from multiprocessing import context
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .forms import CustomUserCreationForm
from django.contrib.auth  import get_user_model

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method=="POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
        return redirect('articles:index')
    else:
        form = AuthenticationForm()
        context = {
            'form':form,
        }
        return render(request, 'accounts/login.html', context)

@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        return redirect('articles:index')

@require_safe
def profile(request, user):
    User = get_user_model()
    person = get_object_or_404(User, username=user)
    context = {
        'person':person,
    }
    return render(request, 'accounts/profile.html', context)


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method=='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')            
    else:
        form = CustomUserCreationForm()
    context = { 
        'form':form,
    }  
    return render(request, 'accounts/signup.html', context)

# def editprofile(request):
#     pass
    # return render(request, 'accounts/editprofile.html')