from django.db import models
from django.contrib.auth.models import User

from .util import eu_header_img


class UserProfile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    eu_id=models.AutoField(primary_key=True)
    header_img=models.ImageField(upload_to=eu_header_img, default='/images/logo.jpg', blank=True, null=True)

    def eu_header_img(self):
        if self.header_img or hasattr(self.header_img, "url"):
            return self.header_img.url
        return '/images/logo.jpg'

