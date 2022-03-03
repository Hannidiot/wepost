<<<<<<< HEAD

=======
>>>>>>> cff26924c6841450a47de7efcad0801cab9b76be
from django.urls import path
from wepost_main.views import views

app_name = 'wepost_main'

urlpatterns = [
<<<<<<< HEAD
    path(r"index/", views.index, name="index"),
    ]


=======
    path("index/", views.index, name="index"),
    path('test/', views.test, name='test'),
]
>>>>>>> cff26924c6841450a47de7efcad0801cab9b76be
