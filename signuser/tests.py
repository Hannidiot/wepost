from django.test import TestCase
from django.contrib.auth.models import User

from signuser.models import *

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
        pass

    def test_unfollow(self):
        pass
