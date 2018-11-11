"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .views import post_list, post_detail, PostListView, post_share

app_name = "blog"

urlpatterns = [
    #path('posts/', post_list, name="posts"),
    path('posts/', PostListView.as_view(), name="posts"),
    path('posts/<slug:slug>/', post_detail, name="post"),
    path('<int:post_id>/share/', post_share, name="post_share"),
]
