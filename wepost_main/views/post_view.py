from django.http import HttpRequest
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from wepost_main.models import *


def post_detail_page(request: HttpRequest, post_id):
    pass


@login_required
def post_edit_page(request: HttpRequest, post_id=None):
    pass

@login_required
def post_delete(request: HttpRequest, post_id=None):
    pass


@login_required
def like(request: HttpRequest, post_id):
    pass


@login_required
def unlike(request: HttpRequest, post_id):
    pass


@login_required
def add_comment(request: HttpRequest, post_id):
    if request.method == 'POST':
        comment = Comment()



@login_required
def delete_comment(request: HttpRequest, post_id, comment_id):
    pass
