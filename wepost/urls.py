"""wepost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
<<<<<<< HEAD
from wepost_main.views import views




=======
from wepost_main.views import test
>>>>>>> cff26924c6841450a47de7efcad0801cab9b76be

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('wepost/', include('wepost_main.urls')),
    path('accounts/', include('allauth.urls')),
    path('', views.index, name="index"),
=======
    path('wepost_main/', include('wepost_main.urls', namespace='wepost_main')),
    path('accounts/', include('allauth.urls')),
>>>>>>> cff26924c6841450a47de7efcad0801cab9b76be
]
