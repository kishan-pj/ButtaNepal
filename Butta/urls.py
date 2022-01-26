from django.urls import path, include
from Butta import views
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

app_name = "Butta"
urlpatterns = [
    path("", views.home, name="Home"),
    path("index/", views.index,name="index"),
    path("register/", views.register, name="register"),
    path("login/", views.login_user, name="login"),
    path(
        "favicon.ico",
        RedirectView.as_view(url=staticfiles_storage.url("/favicon.ico")),
    ),
    path("aboutus/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("logout/", views.logout, name="logout"),
    path("update/<customer_id>",views.update,name="update")
]
