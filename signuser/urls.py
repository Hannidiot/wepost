from django.urls import path, re_path
from . import views

app_name = 'signuser'

urlpatterns = [
    path("views_signuser_profile/", views.views_signuser_profile, name="views_signuser_profile"),
    path("headerimg/", views.views_signuser_header_img, name="views_signuser_headerimg"),
]