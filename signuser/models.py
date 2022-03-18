from django.db import models
from django.contrib.auth.models import User

from .utils import eu_header_img


class UserProfile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    eu_id=models.AutoField(primary_key=True)
    header_img=models.ImageField(upload_to=eu_header_img, default='/images/logo.jpg', blank=True, null=True)


class UserRelation(models.Model):
    followed_user = models.ForeignKey(to=User, on_delete=models.DO_NOTHING, related_name="followed_user")
    follower = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="follower")