from django.http import HttpRequest, HttpResponse
from django.shortcuts import render






# Create your views here.
def index(requset):
    return render(requset,'base.html')


# test response
def test(request: HttpRequest):
    return render(request, 'wepost_main/test.html')
