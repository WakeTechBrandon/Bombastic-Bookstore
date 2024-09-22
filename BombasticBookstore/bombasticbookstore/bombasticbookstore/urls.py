"""
URL configuration for bombasticbookstore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
<<<<<<< HEAD
from usersettings import views as usersettings_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("book_app.urls")),
    path('usersettings/', include('usersettings.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
=======


urlpatterns = [
    path('admin/', admin.site.urls),
    path("book_app/", include("book_app.urls")),
>>>>>>> 94b2799852eeac57fcb090cf09f74b132bb1a437
]
