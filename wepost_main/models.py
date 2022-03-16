from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    poster = models.ForeignKey(to=User)
    title = models.CharField(max_length=120)
    description = models.TextField()
    picture = models.ImageField(upload_to="post_images")
    post_time = models.TimeField()
