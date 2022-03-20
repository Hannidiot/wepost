

from django import forms
from django.contrib.auth.models import User

from signuser.models import UserProfile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["password","username", "email", "first_name", "last_name"]


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['intro', 'gender', 'birthday', 'header_img']