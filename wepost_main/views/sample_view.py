from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# test response
def test(request: HttpRequest):
    return render(request, 'wepost_main/test.html')
