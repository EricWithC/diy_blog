from django.shortcuts import render ,get_object_or_404
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from blog.models import Post, Comment

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