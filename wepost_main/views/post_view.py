from django.http import HttpRequest, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from signuser.models import UserRelation


from wepost_main.models import *
from wepost_main.forms import *


def post_detail_page(request: HttpRequest, post_id):
    user = request.user
    post = Post.objects.get(id=post_id)
    comments = Comment.objects.filter(post_id=post.id).order_by('-comment_time')
    context = {
        'post': post,
        'comments': comments
    }

    if user != "AnonymousUser":
        ur = UserRelation.objects.filter(followed_user_id=post.user_id, follower_id=user.id)
        like = Like.objects.filter(post_id=post.id, user_id=user.id)
        context["is_followed"] = len(ur) != 0
        context["is_liked"] = len(like) != 0
    return render(request, "wepost_main/post_detail.html", context)


@login_required
def post_edit(request: HttpRequest, post_id):
    post = Post.objects.get(id=post_id)
    form = PostForm(instance=post)
    user = request.user

    if post.user_id != user.id:
        return redirect(reverse("index"))

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = user.id
            post.save()

            return redirect(reverse("wepost_main:post_detail", kwargs={"post_id": post_id}))

    return render(request, "wepost_main/post_edit.html", {"form": form})


@login_required
def post_create(request: HttpRequest):
    form = PostForm()
    user = request.user

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = user.id
            post.save()

            return redirect(reverse('wepost_main:post_detail', kwargs={"post_id": post.id}))

    return render(request, "wepost_main/post_edit.html", {"form": form})


@login_required
def post_delete(request: HttpRequest, post_id):
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        user = request.user
        if post == None: return JsonResponse({"status": "fail", "msg": "post doesn't exist"})
        if post.user_id != user.id: return JsonResponse({"status": "fail", "msg": "you dont have the perimission to do this"})

        post.delete()
        return JsonResponse({"status": "success", "msg": ""})

    return redirect(reverse("wepost_main:explore"))


@login_required
def like(request: HttpRequest, post_id):
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        if post == None: return JsonResponse({"status": "fail", "msg": "post doesn't exist"})

        user = request.user
        like = Like.objects.filter(post_id=post.id, user_id=user.id)
        if len(like) != 0: return JsonResponse({"status": "fail", "msg": "already liked this post"})

        like = Like(post_id=post.id, user_id=user.id)
        like.save()

        post.likes += 1
        post.save()

        return JsonResponse({"status": "success", "msg": ""})

    return redirect(reverse("wepost_main:explore"))


@login_required
def unlike(request: HttpRequest, post_id):
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        if post == None: return JsonResponse({"status": "fail", "msg": "post doesn't exist"})

        user = request.user
        like = Like.objects.filter(post_id=post.id, user_id=user.id)
        if len(like) == 0: return JsonResponse({"status": "fail", "msg": "not liked this post"})

        like[0].delete()

        post.likes -= 1
        post.save()

        return JsonResponse({"status": "success", "msg": ""})

    return redirect(reverse("index"))


def get_comments(request: HttpRequest, post_id):
    comments = Comment.objects.filter(post_id=post_id).select_related("user__userprofile")
    context = {
        "comments": comments
    }
    
    return render(request, "components/comment_list.html", context)


@login_required
def add_comment(request: HttpRequest, post_id):
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        if (post == None): return JsonResponse({"status": "fail", "msg": "post doesn't exist"})
        
        user = request.user
        content = request.POST.get("content")
        comment = Comment(user=user, post=post, content=content)
        comment.save()

        post.comments += 1
        post.save()

        return JsonResponse({"status": "success", "msg": ""})

    return redirect(reverse("index"))



@login_required
def delete_comment(request: HttpRequest, post_id, comment_id):
    if request.method == 'POST':
        comment = Comment.objects.get(id=comment_id)
        user = request.user

        if comment == None: return JsonResponse({"status": "fail", "msg": "comment doesnt exist."})
        if comment.user_id != user.id: return JsonResponse({"status": "fail", "msg": "you dont have permission to delete this comment."})

        comment.delete()

        post = Post.objects.get(id=post_id)
        if post != None:
            post.comments -= 1
            post.save()

        return JsonResponse({"status": "success", "msg": ""})

    return redirect(reverse("index"))
