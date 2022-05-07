from django.urls import path
from . import views

app_name='accounts'
urlpatterns = [
    path('login/',views.login, name="login"),
    path('logout/',views.logout, name="logout"),
    path('signup/',views.signup, name="signup"),
    path('<user>/',views.profile, name="profile"),
    path('<user>/editprofile/',views.editprofile, name="editprofile"),
]
