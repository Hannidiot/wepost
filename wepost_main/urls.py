
from django.urls import path
from wepost_main.views import sample_view
from .views import sample_view
app_name = 'wepost_main'

urlpatterns = [
    path("index/", sample_view.index, name="index"),
    path('test/', sample_view.test, name='test'),
]

