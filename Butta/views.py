from django.shortcuts import render, HttpResponse
from django.urls.conf import include


def index(request):
    return render(request, "index.html")


def register(request):
    return render(request, "Register/register.html")


def login(request):
    return render(request, "Login/login.html")

def about(request):
    return render(request, "aboutUs/aboutus.html")