from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# a test response
def test_response(request: HttpRequest):
    return HttpResponse()
