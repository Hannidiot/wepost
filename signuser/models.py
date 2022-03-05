from django.db import models
import os
from django.contrib.auth.models import User

def eu_header_img(instance, filename):
    ext = filename.split('.').pop()
    filename = '{0}{1}.{2}'.format(instance.user.username, instance.eu_id, ext)
    path = os.path.join(instance.user.username, filename)
    return path

# Create your models here.
class UserProfile(models.Model):
    eu_id=models.AutoField(primary_key=True)
    header_img=models.ImageField(upload_to=eu_header_img, default='/images/logo.jpg', blank=True, null=True)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)

    def eu_header_img(self):
        if self.header_img or hasattr(self.header_img, "url"):
            return self.header_img.url
        return '/images/logo.jpg'

