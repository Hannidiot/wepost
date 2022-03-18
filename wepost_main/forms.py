from django import forms
from wepost_main.models import *


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'description', 'picture')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content', )
