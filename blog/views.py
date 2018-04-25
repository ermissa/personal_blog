from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts,Comments
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator,EmptyPage

def homepage(request):
    return render(request,'homepage.html')

def getPosts(request,selected_page=1):
#    latest_post = Posts.objects.get(id=1)
    posts = Posts.objects.all().order_by('-pub_date')
    pages = Paginator(posts,5) #Show 5 post per page
    try:
        returned_page = pages.page(selected_page)
    except EmptyPage:
        returned_page = pages.page(pages.num_pages)
    #content = pages.page(selected_page)    
    return render(request,'blog.html',{'page':returned_page,
                                       'posts':returned_page.object_list
                                        })

def postDetailPage(request,slug):
    post = get_object_or_404(Posts, slug=slug)
    return render(request, 'post_detail.html', {'post':post})
