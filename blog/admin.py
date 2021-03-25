from django.contrib import admin
from blog.models import Post, Blogger, Comment

admin.site.register(Comment)
admin.site.register(Blogger)

class PostCommentInline(admin.TabularInline):
    model = Comment
    max_num = 0

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'blogger', 'post_date')
    inlines = [PostCommentInline]