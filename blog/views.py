from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts,Comments

def index(request):
    taken_posts = Posts.objects.order_by('-pub_date')[:2]
    return HttpResponse("Hello W0r1d")

def blogHomePage(request):
#    latest_post = Posts.objects.get(id=1)
    latest_post = Posts.objects.all()    
    context = {'context':latest_post}
    return render(request,'blog.html',context)