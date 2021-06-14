from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase
from django.contrib.auth.models import User
from blog.models import *


# Include an appropriate `Authorization:` header on all requests.


class ApiTestCase(APITestCase):

    def setUp(self):
        # token = Token.objects.get(user__username='devsia')
        self.user = User.objects.create_user(
            username='user@foo.com', email='user@foo.com', password='top_secret')
        self.token = Token.objects.create(user=self.user)
        self.token.save()

        self.token = Token.objects.get(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        t1 = Tag.objects.create(title='test1', slug='test-one')
        t2 = Tag.objects.create(title='test2', slug='test-two')
        p1 = Post.objects.create(
            title='Тест post one 1', body='test post one')
        p1.tags.set([t1, t2])
        p2 = Post.objects.create(
            title='Тестовый пост 211235 two что-то!,.; там', body='test post two')
        c1 = Comment.objects.create(
            author_name='tester', text='test text', post=p1, approved_comment=True)

    def test_get_posts(self):
        response = self.client.get('/blog/api/posts/', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_post_posts_within_token(self):
        response = self.client.post(
            '/blog/api/posts/', data={'title': 'test new post', 'body': 'test body'})
        self.assertEqual(response.status_code, 201)

    def test_post_posts_without_token(self):
        self.client.credentials()
        response = self.client.post(
            '/blog/api/posts/', data={'title': 'test new post', 'body': 'test body'})
        self.assertEqual(response.status_code, 401)

    def test_patch_posts_within_token(self):
        response = self.client.patch(
            '/blog/api/posts/1/', data={'title': 'test new post', 'body': 'test body'})
        self.assertEqual(response.status_code, 200)

    def test_patch_posts_without_token(self):
        self.client.credentials()
        response = self.client.patch(
            '/blog/api/posts/1/', data={'title': 'test new post', 'body': 'test body'})
        self.assertEqual(response.status_code, 401)

    def test_delete_posts_within_token(self):
        response = self.client.delete(
            '/blog/api/posts/1/')
        self.assertEqual(response.status_code, 204)

    def test_delete_posts_without_token(self):
        self.client.credentials()
        response = self.client.delete(
            '/blog/api/posts/1/')
        self.assertEqual(response.status_code, 401)

    def test_get_tags(self):
        response = self.client.get('/blog/api/tags/', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_post_tags_within_token(self):
        response = self.client.post(
            '/blog/api/tags/', data={'title': 'test new tag', 'slug': 'test-slug'})
        self.assertEqual(response.status_code, 201)

    def test_post_tags_without_token(self):
        self.client.credentials()
        response = self.client.post(
            '/blog/api/tags/', data={'title': 'test new tag', 'slug': 'test-slug'})
        self.assertEqual(response.status_code, 401)

    def test_patch_tags_within_token(self):
        response = self.client.patch(
            '/blog/api/tags/1/', data={'title': 'patch'})
        self.assertEqual(response.status_code, 200)

    def test_patch_tags_without_token(self):
        self.client.credentials()
        response = self.client.patch(
            '/blog/api/tags/1/', data={'title': 'patch'})
        self.assertEqual(response.status_code, 401)

    def test_delete_tags_within_token(self):
        response = self.client.delete(
            '/blog/api/tags/1/')
        self.assertEqual(response.status_code, 204)

    def test_delete_tags_without_token(self):
        self.client.credentials()
        response = self.client.delete(
            '/blog/api/tags/1/')
        self.assertEqual(response.status_code, 401)

    def test_get_comments(self):
        response = self.client.get('/blog/api/comments/', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_post_comments_without_token(self):
        self.client.credentials()
        response = self.client.post(
            '/blog/api/comments/', data={'post': 1,
                                         'author_name': 'api',
                                         'text': 'test post'})
        self.assertEqual(response.status_code, 201)

    def test_patch_comments_within_token(self):
        response = self.client.patch(
            '/blog/api/comments/1/', data={'approved_comment': True})
        self.assertEqual(response.status_code, 200)

    def test_patch_comments_without_token(self):
        self.client.credentials()
        response = self.client.patch(
            '/blog/api/comments/1/', data={'approved_comment': True})
        self.assertEqual(response.status_code, 401)

    def test_delete_comments_within_token(self):
        response = self.client.delete(
            '/blog/api/comments/1/')
        self.assertEqual(response.status_code, 204)

    def test_delete_comments_without_token(self):
        self.client.credentials()
        response = self.client.delete(
            '/blog/api/comments/1/')
        self.assertEqual(response.status_code, 401)
