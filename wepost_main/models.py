from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=120)
    description = models.TextField(default="")
    picture = models.ImageField(upload_to="post_images")
    post_time = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)


class Like(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    like_time = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    content = models.TextField(default="")
    comment_time = models.DateTimeField(auto_now=True)
