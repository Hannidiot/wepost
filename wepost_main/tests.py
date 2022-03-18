from django.test import TestCase
from django.urls import reverse

import os

from wepost_main.models import *
from signuser.tests import create_test_user
from populate_script import populate, IMAGE_DIR

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


class LikeApiTest(TestCase):

    def test_like_when_no_login(self):
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

        temp_likes = post.likes
        post = Post.objects.get(title="cat2")
        self.assertEqual(temp_likes + 1, post.likes)

    def test_unlike(self):
        populate()
        self.client.login(username="test_viewer", password="test")
        
        post = Post.objects.get(title="cat1")
        response = self.client.post(reverse("wepost_main:unlike", kwargs={"post_id": post.id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "success")

        temp_likes = post.likes
        post = Post.objects.get(title="cat1")
        self.assertEqual(temp_likes - 1, post.likes)

    def test_unlike_when_no_like(self):
        populate()
        self.client.login(username="test_viewer", password="test")

        post = Post.objects.get(title="cat2")
        response = self.client.post(reverse("wepost_main:unlike", kwargs={"post_id": post.id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "fail")


class CommentApiTest(TestCase):

    def test_add_comment(self):
        populate()

        self.client.login(username="test_commentor", password="test")
        post = Post.objects.get(title="cat2")
        content = "Irure laboris excepteur ullamco ullamco laboris."
        response = self.client.post(reverse("wepost_main:comment_add", kwargs={"post_id": post.id}),
                                    {"content": content})
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "success")

        temp_comments = post.comments
        post = Post.objects.get(title="cat2")
        self.assertEqual(temp_comments + 1, post.comments)

    def test_delete_comment(self):
        populate()
        self.client.login(username="test_commentor", password="test")

        user = User.objects.get(username="test_commentor")
        post = Post.objects.get(title="cat1")
        comment = Comment.objects.get(user_id=user.id, post_id=post.id)
        response = self.client.post(reverse("wepost_main:comment_delete", 
                kwargs={"post_id": post.id, "comment_id": comment.id}))
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "success")

    def test_delete_others_comment(self):
        populate()
        self.client.login(username="test_viewer", password="test")

        user = User.objects.get(username="test_commentor")
        post = Post.objects.get(title="cat1")
        comment = Comment.objects.get(user_id=user.id, post_id=post.id)
        response = self.client.post(reverse("wepost_main:comment_delete", 
                kwargs={"post_id": post.id, "comment_id": comment.id}))
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "fail")


class PostApiTest(TestCase):
    
    def test_create_post(self):
        populate()
        self.client.login(username="test_poster", password="test")

        new_post = {
            "title": "test_upload_cat",
            "description": "Esse officia enim est officia.",
            "picture": open(os.path.join(IMAGE_DIR, "cat3.jpeg"), 'rb').read()
        }

        response = self.client.post(reverse("wepost_main:post_create"), new_post)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "success")

        posts = Post.objects.all()
        self.assertEqual(len(posts), 4)


    def test_delete_post(self):
        populate()
        self.client.login(username="test_poster", password="test")
        
        post = Post.objects.get(title="cat2")
        response = self.client.post(reverse("wepost_main:post_delete", kwargs={"post_id": post.id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "success")

        posts = Post.objects.all()
        self.assertEqual(len(posts), 2)


    def test_edit_post(self):
        populate()
        self.client.login(username="test_poster", password="test")

        post = Post.objects.get(title="cat2")
        new_post = {
            "title": "test_edit_cat",
            "description": "Esse officia enim est officia.",
            "picture": post.picture
        }
        response = self.client.post(reverse("wepost_main:post_edit", kwargs={"post_id": post.id}), new_post)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "success")

        post = Post.objects.get(title="cat2")
        self.assertEqual(post.title, "test_edit_cat")
