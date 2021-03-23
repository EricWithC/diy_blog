from django.shortcuts import render
from django.views import generic

from blog.models import Post, Blogger

def index(request):
    """View function for home page of website"""
    latest_posts = Post.objects.all()[:3]

    context = {
        'latest_posts': latest_posts
    }
    
    return render(request, 'index.html', context)

class PostListView(generic.ListView):
    model = Post
    paginate_by = 5

class PostDetailView(generic.DetailView):
    model = Post

class BloggerListView(generic.ListView):
    model = Blogger
    paginate_by = 5

class BloggerDetailView(generic.DetailView):
    model = Blogger