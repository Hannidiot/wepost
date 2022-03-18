from django.http import HttpRequest
from django.shortcuts import render, redirect

from .forms import UserForm
from django.contrib.auth.decorators import login_required


@login_required
def user_profile(request: HttpRequest, user_id):
    if request.method == "POST":

        user_form = UserForm(request.POST, instance=request.user)
        if user_form.is_valid():

            user_form.save()
        else: print(user_form.errors)
    return render(request, "account/author_profile.html")


@login_required
def views_signuser_header_img(request):
    header_img = request.FILES['header_img']
    user_profile = request.user.userprofile
    user_profile.header_img = header_img
    user_profile.save()
    return render(request, "account/author_profile.html")


@login_required
def follow(request: HttpRequest, user_id):
    if request.method == 'POST':
        pass

    return redirect("index")


@login_required
def unfollow(request: HttpRequest, user_id):
    if request.method == 'POST':
        pass

    return redirect("index")
