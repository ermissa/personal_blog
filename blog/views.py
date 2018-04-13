from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts,Comments
from django.shortcuts import get_object_or_404

def homepage(request):
    return render(request,'homepage.html')

def blogHomePage(request):
#    latest_post = Posts.objects.get(id=1)
    latest_post = Posts.objects.all()
    context = {'context':latest_post}
    return render(request,'blog.html',context)

def postDetailPage(request,slug):
    post = get_object_or_404(Posts, slug=slug)
    return render(request, 'post_detail.html', {'post':post})
