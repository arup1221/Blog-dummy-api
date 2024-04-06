
from django.contrib import admin
from django.urls import path, include
from blog.views import BlogView, PublicBlog

urlpatterns = [

    path('home/', BlogView.as_view(), name='blog'),
    path('list/', PublicBlog.as_view(), name='public_blog'),

]
