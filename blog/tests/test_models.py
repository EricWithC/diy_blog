from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Blogger, Comment

class PostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(username="testuser", password="password1")
        test_blogger = Blogger.objects.create(user=test_user, bio="testing man")
        Post.objects.create(title="test title", body="Just a test", blogger=test_blogger)
    
    def test_title_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_body_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('body').verbose_name
        self.assertEqual(field_label, 'body')

    def test_blogger_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('blogger').verbose_name
        self.assertEqual(field_label, 'blogger')

    def test_title_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)

    def test_object_name_is_title(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.title}'
        self.assertEqual(expected_object_name, str(post))
    
    def test_get_absolute_url(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.get_absolute_url(), '/blog/post/1')
    
class BloggerTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(username="testuser", password="password1")
        Blogger.objects.create(user=test_user, bio="Just a test bio")

    def test_user_label(self):
        blogger = Blogger.objects.get(id=1)
        field_label = blogger._meta.get_field('user').verbose_name
        self.assertEqual(field_label, 'user')

    def test_bio_label(self):
        blogger = Blogger.objects.get(id=1)
        field_label = blogger._meta.get_field('bio').verbose_name
        self.assertEqual(field_label, 'bio')

    def test_bio_max_length(self):
        blogger = Blogger.objects.get(id=1)
        max_length = blogger._meta.get_field('bio').max_length
        self.assertEqual(max_length, 500)

    def test_object_name_is_username(self):
        blogger = Blogger.objects.get(id=1)
        expected_object_name = f'{blogger.user.username}'
        self.assertEqual(expected_object_name, str(blogger))

    def test_get_absolute_url(self):
        blogger = Blogger.objects.get(id=1)
        self.assertEqual(blogger.get_absolute_url(), '/blog/blogger/1')

class CommentTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create_user(username="testuser1", password="password1")
        test_user2 = User.objects.create_user(username="testuser2", password="password2")
        test_blogger = Blogger.objects.create(user=test_user1, bio="testing man")
        test_post = Post.objects.create(title="test title", body="Just a test", blogger=test_blogger)
        Comment.objects.create(body="Just a test commentbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb", post=test_post, author=test_user2)
        Comment.objects.create(body="Just a test comment", post=test_post, author=test_user1)

    def test_body_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('body').verbose_name
        self.assertEqual(field_label, 'body')

    def test_post_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('post').verbose_name
        self.assertEqual(field_label, 'post')

    def test_author_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('author').verbose_name
        self.assertEqual(field_label, 'author')

    def test_body_max_length(self):
        comment = Comment.objects.get(id=1)
        max_length = comment._meta.get_field('body').max_length
        self.assertEqual(max_length, 500)

    len_title = 75
    def test_object_name_is_body_with_object_title_less_than_or_equal_to_len_title(self):
        comment = Comment.objects.get(id=2)
        expected_object_name = f'{comment.body}'
        self.assertTrue(len(expected_object_name) <= self.len_title)
        self.assertEqual(expected_object_name, str(comment))

    def test_object_name_is_body_with_object_title_greater_than_len_title(self):
        comment = Comment.objects.get(id=1)
        expected_object_name = f'{comment.body}'
        self.assertTrue(len(expected_object_name) > self.len_title)
        self.assertEqual(expected_object_name[:self.len_title] + '...', str(comment))
      