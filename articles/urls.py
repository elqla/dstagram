from django.urls import path
from . import views

app_name='articles'
urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    # 삭제, 수정
    path('<int:pk>/', views.detail, name="detail"),
    path('<int:pk>/comments/', views.comment_create, name="comment_create"),
    
]
