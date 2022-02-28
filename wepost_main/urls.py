from wepost_main import views

from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('test/', views.test, name='test'),
]