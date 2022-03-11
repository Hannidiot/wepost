
from django.urls import path
import wepost_main.views as views
app_name = 'wepost_main'

urlpatterns = [
    path('test/', views.test, name='test'),
    path('home/', views.trending_page, name='trending'),
    path('explore/', views.explore_page, name='explore'),
    path("index/", views.sample_view.index, name="index"),
]

