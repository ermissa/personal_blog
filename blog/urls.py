from django.urls import path,include
from django.contrib import admin

from . import views

urlpatterns = [
    path('',views.blogHomePage,name="bloghome"),
    path('postread',views.postReadPage,name="postread")
]

