from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts,Comments

def homepage(request):
    return render(request,'homepage.html')

def blogHomePage(request):
#    latest_post = Posts.objects.get(id=1)
    latest_post = Posts.objects.all()    
    context = {'context':latest_post}
    return render(request,'blog.html',context)

def postReadPage(request):
    return render(request,'post_read.html')