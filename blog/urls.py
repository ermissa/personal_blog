from django.urls import path,include
from django.contrib import admin

from . import views

urlpatterns = [
    path(r'^$',views.getPosts,name="bloghome"),
    path(r'^(?P<selected_page>\d+)/?$',views.getPosts,name="bloghome"),    
    #path('',views.blogHomePage,name="bloghome"),
    path('<slug>',views.postDetailPage,name="post_detail")
]

