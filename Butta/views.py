from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from django.urls.conf import include
from django.contrib.auth import login
from Butta.models import *
from Butta.forms import *
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


def index(request):
    email = request.session["email"]
    user = Customer.objects.get(email=email)
    if request.method == "POST":
        contact = ContactForm(request.POST)
        print(contact)
        if contact.is_valid():
            contact.save()
            return redirect("/")
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
        try:
            user = Customer.objects.get(email=email, password=password)
            if user is not None:
                Customer.objects.filter(email=email).update(is_login=True)
                return redirect("/index/")
            else:
                messages.error("Sorry!Invalid Credential.")
                return redirect("/login/")
        except:
            messages.error("Sorry! User is not register")
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
    if request.method == "POST":
        contact = ContactForm(request.POST)
        print(contact)
        if contact.is_valid():
            contact.save()
            return redirect("/")
    return render(request, "index.html")


def update(request, customer_id):
    user = Customer.objects.get(customer_id=customer_id)
    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES, instance=user)
        form.save()
        return redirect("/login/")

    return render(request, "update/updateprofile.html", {"user": user})


def product(request):
    product = Product.objects.all()
    return render(request, "product.html", {"product": product})


def contact(request):

    return render(request, "contact_form/contact_form.html")


def checkout(request):
    if request.method == "POST":

        emailaddress = request.POST.get("email")
        name = request.POST.get("fullname")
        template = render_to_string("email/email.html", {"name": name})
        email = EmailMessage(
            "Thank you for choosing our website!",
            template,
            settings.EMAIL_HOST_USER,
            [emailaddress],
        )
        email.fail_sliently = False
        email.send()
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/thankyou/")
    else:
        return render(request, "CheckoutPage/checkout.html")


def productpage(request, user):
    user_data = Customer.objects.get(customer_id=user)
    data = Customer.objects.all()
    if request.method == "POST":
        if user_data.is_login == True:
            review_data = request.POST["review"]
            review_update = Customer.objects.filter(customer_id=user).update(
                review=review_data
            )
            # user_form = CustomerForm(review_data, instance=user_data)
            # user_form.save()
            return redirect("/index/")
        else:
            messages.error("Sorry! You can't comment. First you have to login")
    else:
        return render(
            request, "ProductPage/viewproduct.html", {"data": data, "user": user_data}
        )


def thankyou(request):
    request.session.flush()
    return render(request, "ThankYouPage/thankyou.html")


def productPage(request):
    data = Customer.objects.all()
    return render(request, "ProductPage/viewproduct.html", {"data": data})
