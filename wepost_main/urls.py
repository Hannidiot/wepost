from django.urls import path
from wepost_main.views import views

app_name = 'wepost_main'

urlpatterns = [
    path(r"index/", views.index, name="index"),
]