from os import name
from django.contrib import admin
from django.urls import path, include
from Butta import views
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

app_name = "Butta"
urlpatterns = [
    path("", views.index, name="Home"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path(
        "favicon.ico",
        RedirectView.as_view(url=staticfiles_storage.url("/favicon.ico")),
    ),
    path("aboutus/",views.about, name="about"),
]
