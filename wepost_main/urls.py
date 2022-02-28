from django.contrib import admin
from django.urls import path

from wepost_main.views import sample_view

urlpatterns = [
    path('', sample_view),
]