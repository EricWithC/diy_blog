from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.PostListView.as_view(), name='all-posts'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/comment/', views.CommentCreate.as_view(), name='comment-create'),
]