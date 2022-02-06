
from django.shortcuts import render, HttpResponse,redirect
from django.urls.conf import include
from django.contrib.auth import login
from Butta.models import Customer
from . forms import CustomerForms

def index(request):
    return render(request, "index.html")


def register(request):
    print(request)
    if request.method == "POST":
        form = CustomerForms(request.POST)
        if form.is_valid():
                form.save()
                print(form)
                return redirect("/login/")
        else:
                print("Details Invalid")
    return render(request, "Register/register.html")


def login_user(request):
    if request.method == "POST":
        email = request.POST['email']
        customer_password = request.POST['customer_password']
        user = Customer.objects.get(email = email,customer_password = customer_password)
        if user is not None:
            # login(request,user)
            request.session['email']=email
            print(request.session['email'])
            return redirect("/")
        
    return render(request, "Login/login.html")

def about(request):
    return render(request, "aboutUs/aboutus.html")

def contact(request):
    return render(request, "contact_form/contact_form.html")