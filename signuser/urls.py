from django.urls import path
from . import views

app_name = 'signuser'

urlpatterns = [
    path('<user_id>/', views.user_profile, name='user_profile'),
    path('<user_id>/follow/', views.follow, name='follow'),
    path('<user_id>/unfollow/', views.unfollow, name='unfollow'),
    path('<user_id>/edit/', views.user_profile_edit, name="edit_profile"),
    path('<user_id>/<type>/', views.user_profile_content, name="get_user_profile_content"),
]