from django.test import TestCase
from django.urls import reverse

from wepost_main.models import *
from signuser.tests import create_test_user
from populate_script import populate

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


class LikeTest(TestCase):

    def test_like_when_no_user_login(self):
        response = self.client.post(reverse("wepost_main:like", kwargs={"post_id": "123"}))
        self.assertEqual(response.status_code, 302)
        self.assertIn("/accounts/login", response['location'])

    def test_like(self):
        populate()
        self.client.login(username="test_viewer", password="test")
        
        post = Post.objects.get(title="cat2")
        response = self.client.post(reverse("wepost_main:like", kwargs={"post_id": post.id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "success")

    def test_unlike(self):
        populate()
        self.client.login(username="test_viewer", password="test")
        
        post = Post.objects.get(title="cat1")
        response = self.client.post(reverse("wepost_main:unlike", kwargs={"post_id": post.id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "success")

    def test_unlike_when_no_like(self):
        populate()
        self.client.login(username="test_viewer", password="test")

        post = Post.objects.get(title="cat2")
        response = self.client.post(reverse("wepost_main:unlike", kwargs={"post_id": post.id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "fail")
