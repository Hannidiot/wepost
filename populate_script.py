import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'wepost.settings')

import django
django.setup()

import json

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile

from wepost_main.models import *
from signuser.models import *

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
    user_relations = load_json_from_file("relations.json")

    for user in users:
        add_user(**user)

    for post in posts:
        add_post(**post)

    # for like in likes:
    #     add_like(**like)

    for comment in comments:
        add_comment(**comment)

    for relation in user_relations:
        add_user_relation(**relation)


def add_post(username, title, description, pic_name, likes=0, views=0):
    user = User.objects.get_or_create(username=username)[0]

    post = Post.objects.get_or_create(user=user, title=title)[0]
    post.description = description
    post.picture = SimpleUploadedFile(
        name=pic_name,
        content=open(os.path.join(IMAGE_DIR, pic_name), 'rb').read()
        )
    post.likes = likes
    post.views = views
    post.save()

    return post


def add_like(username, post_title):
    user = User.objects.get_or_create(username=username)[0]
    post = Post.objects.get_or_create(title=post_title)[0]

    like = Like.objects.get_or_create(user=user, post=post)[0]
    like.save()

    return like


def add_comment(username, post_title, content):
    user = User.objects.get_or_create(username=username)[0]
    post = Post.objects.get_or_create(title=post_title)[0]

    comment = Comment.objects.get_or_create(user=user, post=post)[0]
    comment.content = content
    comment.save()

    return comment


def add_profile(user, intro, gender, birthday=datetime(1970, 1, 1), header_img=None):
    up = UserProfile.objects.get_or_create(user_id=user.id)[0]
    up.intro = intro
    up.gender = gender
    up.birthday = birthday
    if header_img:
        up.header_img = SimpleUploadedFile(
            name=header_img,
            content=open(os.path.join(IMAGE_DIR, header_img), 'rb').read()
        )
    up.save()
    return up


def add_user_relation(followed, followers):
    followed_user = User.objects.get(username=followed)
    for follower in followers:
        follower_user = User.objects.get(username=follower)
        ur = UserRelation.objects.get_or_create(followed_user_id=followed_user.id, follower_id=follower_user.id)[0]
        ur.save()

        up = UserProfile.objects.get(user_id=followed_user.id)
        up.followers += 1
        up.save()

        up = UserProfile.objects.get(user_id=follower_user.id)
        up.following += 1
        up.save()

def add_user(username, password, email, profile):
    user = User.objects.get_or_create(email=email)[0]

    user.username = username
    user.set_password(password)
    user.save()

    add_profile(user, **profile)

    return user

if __name__ == '__main__':
    populate()
    