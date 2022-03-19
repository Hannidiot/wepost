from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

from .utils import eu_header_img


class UserProfile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    intro = models.CharField(max_length=300)
    gender = models.IntegerField(
        choices=((1, 'male'), (2, 'female'), (3, 'not willing to tell')),
        default=1
    )
    birthday = models.DateField(blank=True, default=datetime(1970, 1, 1))
    header_img = models.ImageField(upload_to=eu_header_img, default='/images/avatar.svg', blank=True, null=True)
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)
    posts = models.IntegerField(default=0)


class UserRelation(models.Model):
    followed_user = models.ForeignKey(to=User, on_delete=models.DO_NOTHING, related_name="followed_user")
    follower = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="follower")
