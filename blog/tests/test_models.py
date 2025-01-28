import unittest
from django.test import TestCase
from blog.models import Post, Comment
from django.utils import timezone

class PostModelTest(TestCase):
    databases = {'test'}

    def setUp(self):
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            content='Test Content',
            author='Test Author',
            status='published',
            published_at=timezone.now()
        )

    def test_post_creation(self):
        self.assertIsInstance(self.post, Post)
        self.assertEqual(self.post.__str__(), self.post.title)

    def test_post_ordering(self):
        posts = Post.objects.all()
        self.assertEqual(posts[0], self.post)

    def test_post_views_default(self):
        self.assertEqual(self.post.views, 0)

class CommentModelTest(TestCase):

    def setUp(self):
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            content='Test Content',
            author='Test Author',
            status='published',
            published_at=timezone.now()
        )
        self.comment = Comment.objects.create(
            post=self.post,
            name='Test Commenter',
            email='test@example.com',
            body='Test Comment',
            active=True
        )

    def test_comment_creation(self):
        self.assertIsInstance(self.comment, Comment)
        self.assertEqual(self.comment.__str__(), f"Comment by {self.comment.name} on {self.comment.post}")

    def test_comment_ordering(self):
        comments = Comment.objects.all()
        self.assertEqual(comments[0], self.comment)

    def test_comment_active_default(self):
        self.assertTrue(self.comment.active)

if __name__ == '__main__':
    unittest.main()