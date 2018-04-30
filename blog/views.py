from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts,Comments
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator,EmptyPage
from django.views.generic import ListView
import logging
logger = logging.getLogger(__name__)

class PostListView(ListView):
    model = Posts
    paginate_by = 3
    template_name = 'blog_classbased.html'

def homepage(request):
    return render(request,'homepage.html')

def Login(request):
    return render(request,'login.html')

def getPosts(request):
    posts = Posts.objects.all()
    pages = Paginator(posts, 3) #Show 3 post per page
    selected_page = request.GET.get('page', 1)
    try:
        returned_page = pages.get_page(selected_page)
    except EmptyPage:
        returned_page = pages.page(pages.num_pages) 
    return render(request,'blog.html',{'page':returned_page,
                                    'posts':returned_page.object_list
                                    })

def postDetailPage(request,slug):
    post = get_object_or_404(Posts, slug=slug)
    return render(request, 'post_detail.html', {'post':post})
