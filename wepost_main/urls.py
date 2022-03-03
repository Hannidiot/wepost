from django.urls import path
from wepost_main.views import views

app_name = 'wepost_main'

urlpatterns = [
    path("index/", views.index, name="index"),
    path('test/', views.test, name='test'),
]