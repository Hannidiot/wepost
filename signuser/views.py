from django.shortcuts import render
from django.views.decorators.gzip import gzip_page
from django.views.decorators.http import require_POST

from .forms import UserForm
# Create your views here.
from django.contrib.auth.decorators import login_required
from . import signals

@gzip_page
@login_required
def views_signuser_profile(request):
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