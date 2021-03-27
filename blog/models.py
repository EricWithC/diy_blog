from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Post(models.Model):
    """Model representing a blog post"""
    title = models.CharField(max_length=200)
    post_date = models.DateField(auto_now_add=True)
    blogger = models.ForeignKey(User, on_delete=models.CASCADE)
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

class Comment(models.Model):
    """Model representing a comment made by a logged in user"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String for representing the Model object"""
        len_title=75
        if len(self.body)>len_title:
            titlestring=self.body[:len_title] + '...'
        else:
            titlestring=self.body
        return titlestring
