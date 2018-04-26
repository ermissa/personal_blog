from django.urls import path,include
from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
    #Regexs are not used in path() function. (This function is New in Django2.0 and the use of this function is encouraged.)#
    path('',views.getPosts,name="bloghome"),
    path('<slug>/',views.postDetailPage,name="post_detail")

    #I am learning when I writing this blog so I decided not to delete following lines. These mistakes maybe beneficial for someone.#
    #! FOR url() FUNCTION : FROM DJANGO DOCUMENTATIONS : "It’s likely to be deprecated in a future release."
    
    #url('',views.getPosts,name="bloghome"),
    #url(r'^(?P<selected_page>\d+)/?$',views.getPosts,name="bloghome"),    
    #url('^<slug>/?',views.postDetailPage,name="post_detail")
    #url(r'^(?P<slug>[\w-]+)/$',views.postDetailPage,name="post_detail")
]

