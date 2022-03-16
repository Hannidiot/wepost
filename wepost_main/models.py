from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    poster = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=120)
    description = models.TextField(default="")
    picture = models.ImageField(upload_to="post_images")
    post_time = models.TimeField()
    like_times = models.IntegerField(default=0)


class LikePost(models.Model):
    post_id = models.ForeignKey(to=Post, on_delete=models.DO_NOTHING)
    uid = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)
    like_time = models.TimeField()

    def save(self, *args, **kwargs):
        post = Post.objects.get()
