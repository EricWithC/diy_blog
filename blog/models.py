from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Post(models.Model):
    """Model representing a blog post"""
    title = models.CharField(max_length=200)
    post_date = models.DateField(auto_now_add=True)
    blogger = models.ForeignKey('Blogger', on_delete=models.CASCADE)
    body = models.TextField()

    class Meta:
        permissions = (('can_edit_posts', 'Add, update or delete a blog post'),)
        ordering = ['-post_date']

    def __str__(self):
        """String for representing the Model object"""
        return self.title
    
    def get_absolute_url(self):
        """Return url to acces detail view of this post"""
        return reverse("post-detail", args=[str(self.id)])

class Blogger(models.Model):
    """Model representing an blogger"""
    first_name = models.CharField(max_length=200, null=True, blank=True)    
    last_name = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=50, unique=True, help_text="Username can contain 50 characters max.")
    bio = models.TextField(max_length=500)

    def __str__(self):
        """String for representing the Model object"""
        return self.username
    
    def get_absolute_url(self):
        """Return url to acces detail view of this post"""
        return reverse("blogger-detail", args=[str(self.id)])

class Comment(models.Model):
    """Model representing a comment made by a logged in user"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String for representing the Model object"""
        return self.username
