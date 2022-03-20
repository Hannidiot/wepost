from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from wepost_main.models import Post

from wepost_main.utils import ajax_login_required

from .forms import UserForm, UserProfileForm
from signuser.models import *


def user_profile_content(request: HttpRequest, user_id, type):
    context = {}
    user = request.user

    if type == "posts":
        posts = Post.objects.filter(user_id=user_id)
        if user != "AnonymousUser":
            for post in posts:
                likes = post.like_set.filter(user_id=user.id)
                post.is_liked = len(likes) != 0

        context['post_list'] = posts
        return render(request, "account/components/post_card_list.html", context)

    elif type == "followers":
        users = UserRelation.objects.select_related("follower", "follower__userprofile").filter(followed_user_id=user_id)
        context['followers'] = users
        return render(request, "account/components/follower_card_list.html", context)

    elif type == "following":
        users = UserRelation.objects.select_related("followed_user", "followed_user__userprofile").filter(follower_id=user_id)
        context['followeds'] = users
        return render(request, "account/components/followed_card_list.html", context)


def user_profile(request: HttpRequest, user_id):
    profile_user = User.objects.select_related("userprofile").get(id=user_id)

    return render(request, "account/user_profile.html", context={"profile_user": profile_user})


@login_required
def user_profile_edit(request: HttpRequest, user_id):
    user_profile = UserProfile.objects.get(user_id=user_id)
    form = UserProfileForm(instance=user_profile)

    if request.method == 'POST':
        pass

    return render(request, "account/user_profile_edit.html", {"form": form})


@ajax_login_required
def follow(request: HttpRequest, user_id):
    if request.method == 'POST':
        login_user = request.user
        followed_user = User.objects.get(id=user_id)

        if (login_user.id == followed_user.id): return JsonResponse({"status": "fail", "msg": "you cannot follow yourself"})

        # check if already followed this user
        is_followed = len(UserRelation.objects.filter(follower_id=login_user.id, followed_user_id=followed_user.id)) == 1
        if (is_followed): return JsonResponse({"status": "fail", "msg": "already followed this user"})

        ur = UserRelation(followed_user_id=followed_user.id, follower_id=login_user.id)
        ur.save()

        up = UserProfile.objects.get(user_id=followed_user.id)
        up.followers += 1
        up.save()

        up = UserProfile.objects.get(user_id=login_user.id)
        up.following += 1
        up.save()

        return JsonResponse({"status": "success", "msg": ""})

    return redirect("index")


@ajax_login_required
def unfollow(request: HttpRequest, user_id):
    if request.method == 'POST':
        login_user = request.user
        followed_user = User.objects.get(id=user_id)

        if (login_user.id == followed_user.id): return JsonResponse({"status": "fail", "msg": "you cannot unfollow yourself"})

        # check if already followed this user
        ur = UserRelation.objects.filter(follower_id=login_user.id, followed_user_id=followed_user.id)
        is_followed = len(ur) == 1
        if (not is_followed): return JsonResponse({"status": "fail", "msg": "you have not followed this user"})

        ur.delete()

        up = UserProfile.objects.get(user_id=followed_user.id)
        up.followers -= 1
        up.save()

        up = UserProfile.objects.get(user_id=login_user.id)
        up.following -= 1
        up.save()

        return JsonResponse({"status": "success", "msg": ""})

    return redirect("index")
