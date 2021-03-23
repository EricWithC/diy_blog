from django.shortcuts import render ,get_object_or_404
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

class BloggerDetailView(generic.ListView):
    model = Post
    template_name = 'blog/blogger_detail.html'
    paginate_by = 5
    
    def get_queryset(self):
        id = self.kwargs['pk']
        target_blogger = get_object_or_404(Blogger, pk = id)
        return Post.objects.filter(blogger=target_blogger)

    def get_context_data(self, **kwargs):
        context = super(BloggerDetailView, self).get_context_data(**kwargs)
        context['blogger'] = get_object_or_404(Blogger, pk = self.kwargs['pk'])
        return context
    