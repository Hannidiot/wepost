
from django.urls import path
import wepost_main.views as views
app_name = 'wepost_main'

urlpatterns = [
    path('test/', views.test, name='test'),
    path('home/', views.trending_page, name='trending'),
    path('explore/', views.explore_page, name='explore'),
    path('explore/albums/', views.load_explore_page_albums, name='explore_albums'),
    path('index/', views.sample_view.index, name='index'),

    path('post/create/', views.post_create, name='post_create'),
    path('post/<post_id>/', views.post_detail_page, name='post_detail'),
    path('post/<post_id>/edit/', views.post_edit, name='post_edit'),
    path('post/<post_id>/delete/', views.post_delete, name='post_delete'),
    path('post/<post_id>/like/', views.like, name='like'),
    path('post/<post_id>/unlike/', views.unlike, name='unlike'),
    path('post/<post_id>/comment/', views.add_comment, name='comment_add'),
    path('post/<post_id>/<comment_id>/delete/', views.delete_comment, name='comment_delete'),
]

