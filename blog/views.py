from django.shortcuts import render ,get_object_or_404
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from blog.models import Post, Blogger, Comment

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

class PostCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Post
    permission_required = 'blog.can_edit_posts'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.blogger = self.request.user.blogger
        return super(PostCreate, self).form_valid(form)

class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['body']

    def get_context_data(self, **kwargs):
        context = super(CommentCreate, self).get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, pk = self.kwargs['pk'])
        return context

    def form_valid(self, form):
        """
        Add author and associated blog to form data before setting it as valid (so it is saved to model)
        """
        #Add logged-in user as author of comment
        form.instance.author = self.request.user
        #Associate comment with blog based on passed id
        form.instance.post=get_object_or_404(Post, pk = self.kwargs['pk'])
        # Call super-class form validation behavior
        return super(CommentCreate, self).form_valid(form)
    
    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.kwargs['pk']})