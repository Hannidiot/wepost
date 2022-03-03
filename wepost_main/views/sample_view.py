from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

<<<<<<< HEAD:wepost_main/views/views.py
# Create your views here.
def index(requset):
    return render(requset,'base.html')
=======

# test response
def test(request: HttpRequest):
    return render(request, 'wepost_main/test.html')
>>>>>>> fix_conflict:wepost_main/views/sample_view.py
