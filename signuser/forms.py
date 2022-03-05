

from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["password","username", "email", "first_name", "last_name", "date_joined"]