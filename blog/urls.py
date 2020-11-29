from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path('', views.showblog, name='showblog'),
    path('<int:post_id>/', views.specific_post, name='specific_post')
]
# Create your views here.
