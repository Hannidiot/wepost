from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse


from wepost_main.utils import JsonResponse
from wepost_main.models import *
from wepost_main.forms import *


def post_detail_page(request: HttpRequest, post_id):
    pass


@login_required
def post_edit(request: HttpRequest, post_id):
    post = Post.objects.get(id=post_id)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            post = form.save(commit=True)

            return redirect(reverse("wepost_main:post_detail", kwargs={"post_id": post_id}))

    return render(request, "wepost_main/post_edit.html", {"form": form})


@login_required
def post_create(request: HttpRequest):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
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
