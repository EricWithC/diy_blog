from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User, Permission

from blog.models import Post, Blogger, Comment

class IndexViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_posts = 12

        test_user = User.objects.create_user(username="testuser", password="password1")
        test_blogger = Blogger.objects.create(user=test_user, bio="testing man")
        for post_num in range(number_of_posts):
            Post.objects.create(
                title=f'test title number {post_num}', 
                body=f'Just a test number {post_num}', 
                blogger=test_blogger
                )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
