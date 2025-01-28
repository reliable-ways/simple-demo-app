import unittest
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm

class BlogViewsTest(TestCase):
    databases = {'test'}

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post = Post.objects.create(title='Test Post', slug='test-post', content='Test Content', status='published')
        self.comment = Comment.objects.create(post=self.post, name='Test Commenter', body='Test Comment', active=True)

    def test_post_create_view_get(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('post_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_form.html')
        self.assertIsInstance(response.context['form'], PostForm)

    def test_post_create_view_post(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('post_create'), {'title': 'New Post', 'content': 'New Content', 'status': 'published'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('post_list'))
        self.assertEqual(Post.objects.count(), 2)

    def test_post_list_view(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_list.html')
        self.assertEqual(len(response.context['posts']), 1)

    def test_post_detail_view_get(self):
        response = self.client.get(reverse('post_detail', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_detail.html')
        self.assertEqual(response.context['post'], self.post)
        self.assertEqual(len(response.context['comments']), 1)
        self.assertIsInstance(response.context['comment_form'], CommentForm)

    def test_post_detail_view_post(self):
        response = self.client.post(reverse('post_detail', args=[self.post.slug]), {'name': 'New Commenter', 'body': 'New Comment'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_detail.html')
        self.assertEqual(Comment.objects.count(), 2)
        self.assertIsNotNone(response.context['new_comment'])

if __name__ == '__main__':
    unittest.main()