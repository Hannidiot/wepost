import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'wepost.settings')

import django
django.setup()

import json

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile

from wepost_main.models import *

BASE_DIR = settings.BASE_DIR
TEST_DIR = os.path.join(BASE_DIR, 'tests')
IMAGE_DIR = os.path.join(TEST_DIR, 'media', 'images')

def load_json_from_file(file_name):
    with open(os.path.join(TEST_DIR, file_name), 'r') as f:
        return json.load(f)

def populate():
    users = load_json_from_file("users.json")
    posts = load_json_from_file("posts.json")
    likes = load_json_from_file("likes.json")
    comments = load_json_from_file("comments.json")

    for user in users:
        add_user(**user)

    for post in posts:
        add_post(**post)

    for like in likes:
        add_like(**like)

    for comment in comments:
        add_comment(**comment)


def add_user(username, password):
    user = User.objects.get_or_create(username=username)[0]

    user.password = password
    user.save()

    return user


def add_post(username, title, description, pic_name, likes=0, views=0):
    user = User.objects.get(username=username)[0]

    post = Post.objects.get_or_create(user=user, title=title)[0]
    post.description = description
    post.picture = SimpleUploadedFile(
        name=pic_name,
        content=open(os.path.join(IMAGE_DIR, pic_name))
        )
    post.likes = likes
    post.views = views
    post.save()

    return post


def add_like(username, post_title):
    user = User.objects.get_or_create(username=username)[0]
    post = Post.objects.get_or_create(user=user, title=post_title)[0]

    like = Like.objects.get_or_create(user=user, post=post)[0]
    like.save()

    return like


def add_comment(username, post_title, content):
    user = User.objects.get(username=username)[0]
    post = Post.objects.get(title=post_title)[0]

    comment = Comment.objects.get_or_create(user=user, post=post)[0]
    comment.content = content
    comment.save()

    return comment
