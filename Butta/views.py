import email
import re
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from django.urls.conf import include
from django.contrib.auth import login
from Butta.models import *
from Butta.forms import *


def index(request):
    email = request.session["email"]
    user = Customer.objects.get(email=email)
    return render(request, "index.html", {"user": user})


def register(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        email = request.POST["email"]
        if form.is_valid():
            print(request)
            if Customer.objects.filter(email=email).exists():
                messages.error(request, "Please! Enter Unique Email Address")
                return redirect("/register/")
            else:
                form.save()
                return redirect("/login/")
    return render(request, "Register/register.html")


def login_user(request):
    if request.method == "POST":
        email = request.session["email"] = request.POST["email"]
        password = request.session["password"] = request.POST["password"]
        user = Customer.objects.get(email=email, password=password)
        if user is not None:
            Customer.objects.filter(email=email).update(is_login=True)
            return redirect("/index/")
        else:
            return redirect("/login/")
    return render(
        request,
        "Login/login.html",
    )


def about(request):
    return render(request, "aboutUs/aboutus.html")


def contact(request):
    return render(request, "contact_form/contact_form.html")


def logout(request):
    request.session.flush()
    return redirect("/")


def home(request):
    return render(request, "index.html")

def update(request,customer_id):
    user = Customer.objects.get(customer_id=customer_id)
    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES, instance=user)
        form.save()
        return redirect("/login/")
    
    return render(request,'update/updateprofile.html',{'user':user})

def product(request):
    product = Product.objects.all()
    return render(request,'product.html',{'product':product})


