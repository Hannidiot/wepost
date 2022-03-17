from django.test import TestCase

from wepost_main.models import *
from signuser.tests import create_user

def create_post(user):
    post = Post()
    post.user = user
    post.title = "test title"
    post.description = "test description"
    post.save()
    return post

def create_like(user, post):
    like = Like()
    like.user = user
    like.post = post
    like.save()
    return like

def create_comment(user, post):
    comment = Comment(user=user,post=post, content="test")
    comment.save()
    return comment


class TestPageTest(TestCase):

    def test_page_returns_correct_html(self):
        response = self.client.get('/wepost/test/')

        self.assertContains(response, "A Test Page appears")
        self.assertTemplateUsed(response, 'wepost_main/test.html')


class BasePageTest(TestCase):
    
    def setUp(self):
        self.response = self.client.get('/wepost/home/')

    def test_default_title(self):
        self.assertContains(self.response, 'Wepost - Post Your Life Moments')

    def test_default_content(self):
        self.assertContains(self.response, 'Place body content here!')


class ExploreTest(TestCase):

    def test_page_returns_correct_html(self):
        response = self.client.get('/wepost/explore/')
        self.assertTemplateUsed(response, 'wepost_main/explore.html')

    def test_navbar_show_correctly(self):
        response = self.client.get('/wepost/explore/')

        self.assertContains(response, "nav")
        self.assertContains(response, "Wepost")

        self.assertContains(response, "Login")


class PostModelTest(TestCase):

    def setUp(self):
        self.user = create_user()

    def test_create(self):
        create_post(self.user)

        posts = Post.objects.all()
        self.assertEqual(len(posts), 1)


class LikeModelTest(TestCase):

    def setUp(self):
        self.user = create_user()
        self.post = create_post(self.user)

    def test_create(self):
        create_like(self.user, self.post)

        self.assertEqual(len(Like.objects.all()), 1)
        self.assertEqual(self.post.likes, 0)

        self.post = Post.objects.get(id=self.post.id)
        self.assertEqual(self.post.likes, 1)

    def test_delete(self):
        self.post = Post.objects.get(id=self.post.id)
        self.assertEqual(self.post.likes, 0)

        like = create_like(self.user, self.post)
        self.post = Post.objects.get(id=self.post.id)
        self.assertEqual(self.post.likes, 1)

        like.delete()
        self.post = Post.objects.get(id=self.post.id)
        self.assertEqual(self.post.likes, 0)


class CommentModelTest(TestCase):

    def setUp(self):
        self.user = create_user()
        self.post = create_post(self.user)

    def test_create(self):
        self.comment = create_comment(self.user, self.post)
        self.assertEqual(len(Comment.objects.all()), 1)