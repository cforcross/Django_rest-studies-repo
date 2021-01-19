from django.test import TestCase
from django.contrib.auth.models import User
# Create your tests here.
from .models import Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(
            username="testuser1", password="abc123"
        )
        # create a block post
        test_post = Post.objects.create(
            author=testuser1, title="Blog tile", body="body content"
        )

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f"{post.author}"
        title = f"{post.title}"
        body = f"{post.body}"
        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'Blog title')
        self.assertEqual(body, "body content")
