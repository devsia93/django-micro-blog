from django.test import TestCase, Client
from blog.models import *


class BlogTestCase(TestCase):

    # constants for equals
    post_autoslug_one = 'test-post-one-1'
    post_autoslug_two = 'testovyj-post-211235-two-chto-to-tam'

    post_absolute_url_one = f'/blog/post/{post_autoslug_one}/'
    post_absolute_url_two = f'/blog/post/{post_autoslug_two}/'

    post_count_approved_comments_one = 1
    post_count_approved_comments_two = 0
    # endconstants

    def setUp(self):
        t1 = Tag.objects.create(title='test1', slug='test-one')
        t2 = Tag.objects.create(title='test2', slug='test-two')
        p1 = Post.objects.create(title='Тест post one 1', body='test post one')
        p1.tags.set([t1, t2])
        p2 = Post.objects.create(
            title='Тестовый пост 211235 two что-то!,.; там', body='test post two')
        c1 = Comment.objects.create(
            author_name='tester', text='test text', post=p1, approved_comment=True)

    def test_valid_autoslug(self):
        p1 = Post.objects.get(pk=1)
        p2 = Post.objects.get(pk=2)
        self.assertTrue(p1.slug == self.post_autoslug_one)
        self.assertTrue(p2.slug == self.post_autoslug_two)

    def test_get_absolute_url(self):
        p1 = Post.objects.get(pk=1)
        p2 = Post.objects.get(pk=2)
        self.assertTrue(p1.get_absolute_url() == self.post_absolute_url_one)
        self.assertTrue(p2.get_absolute_url() == self.post_absolute_url_two)

    def test_check_available_tag(self):
        p1 = Post.objects.get(pk=1)
        p2 = Post.objects.get(pk=2)
        self.assertTrue(p1.check_available_tag())
        self.assertFalse(p2.check_available_tag())

    def test_check_count_approved_comments(self):
        p1 = Post.objects.get(pk=1)
        p2 = Post.objects.get(pk=2)
        self.assertTrue(p1.count_of_approved_comments() ==
                        self.post_count_approved_comments_one)
        self.assertTrue(p2.count_of_approved_comments() ==
                        self.post_count_approved_comments_two)

    def test_post_view(self):
        c = Client()
        response = c.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['page_object']), 2)

    def test_tag_view(self):
        c = Client()
        response = c.get('/blog/tags/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['tags']), 2)

    def test_comment_view(self):
        c = Client()
        response = c.get(self.post_absolute_url_one)
        post = response.context['post']
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(post.comments.all()), 1)
