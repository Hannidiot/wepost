from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from signuser.models import *
from populate_script import populate


def create_test_user():
    user = User.objects.get_or_create(username="test")
    user.set_password("test")
    user.save()
    return user

class UserProfileTest(TestCase):

    def test_create(self):
        pass


class UserRelationModelTest(TestCase):
    
    def test_follow(self):
        populate()
        create_test_user()

        self.client.login(username="test", password="test")

        user = User.objects.get(username="test_poster")
        response = self.client.post(reverse("signuser:follow", kwargs={"user_id": user.id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "success")

        up = UserProfile.objects.get(user_id=user.id)
        self.assertEqual(up.followers, 3)

    def test_unfollow(self):
        populate()
        create_test_user()

        self.client.login(username="test_viewer", password="test")

        user = User.objects.get(username="test_poster")
        response = self.client.post(reverse("signuser:unfollow", kwargs={"user_id": user.id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "success")

        up = UserProfile.objects.get(user_id=user.id)
        self.assertEqual(up.followers, 1)


class LoginTest(TestCase):

    def test_login(self):
        populate()

        is_logged_in = self.client.login(username="test_viewer", password="test")
        self.assertTrue(is_logged_in)
