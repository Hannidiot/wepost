from django.test import TestCase
from django.contrib.auth.models import User

from signuser.models import *
from populate_script import populate

def create_test_user():
    user = User()
    user.username = "test"
    user.password = "test"
    user.save()
    return user

class UserProfileTest(TestCase):

    def test_create(self):
        pass


class UserRelationModelTest(TestCase):
    
    def test_follow(self):
        populate()

    def test_unfollow(self):
        populate()


class LoginTest(TestCase):

    def test_login(self):
        populate()

        is_logged_in = self.client.login(username="test_viewer", password="test")
        self.assertTrue(is_logged_in)
