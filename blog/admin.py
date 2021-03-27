from django.contrib import admin
from blog.models import Post, Comment

admin.site.register(Comment)

class PostCommentInline(admin.TabularInline):
    model = Comment
    max_num = 0

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'post_date')
    inlines = [PostCommentInline]