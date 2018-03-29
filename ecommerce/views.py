from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm
from .forms import LoginForm
from .forms import RegisterForm

from django.contrib.auth import get_user_model

def home_page(request):
    # add different context here
    context = {
        "title": "This is from context of home page",
        "content": "Home Page"
    }
    if request.user.is_authenticated():
        name = request.user.username
        context["premium_content"] = "Yeahh.. Hello "+name
    return render(request, "home_page.html", context)

def about_page(request):
    context = {
        "title": "This is from context of about page",
        "content": "About Page"
    }
    return render(request, "home_page.html", context)

# make ContactForm for this
def contact_page(request):
    # contact form class instance
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "This is from context of contact page",
        "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    return render(request, "contact/contact.html", context)


# make LoginForm for this
def login_page(request):
    # create instance of LoginForm
    login_form = LoginForm(request.POST or None)
    context = {
        "form": login_form
    }

    if login_form.is_valid():
        print(login_form.cleaned_data)
        username = login_form.cleaned_data.get("username")
        password = login_form.cleaned_data.get("password")
        user = authenticate(username= username, password= password)
        print("user logged in")
        print(request.user.is_authenticated())

        if user is not None:
            # login function for making the user login
            login(request, user) # makes the user Login
            context['form'] = LoginForm()
            # redirect to a success page
            print("user logged in")
            print(request.user.is_authenticated())
            return redirect("/")
        else:
            print("Error in authentication...")

    return render(request, "auth/login.html", context)

User = get_user_model()
# make RegisterForm for this
def register_page(request):
    # create instance of RegisterForm
    register_form = RegisterForm(request.POST or None)
    context = {
        "form": register_form
    }
    
    if register_form.is_valid():
        print(register_form.cleaned_data)
        username= register_form.cleaned_data.get("username")
        email= register_form.cleaned_data.get("email")
        password= register_form.cleaned_data.get("password")
        # creating new user and add it to our User Model
        new_user = User.objects.create_user(username, email, password)
        print(new_user)

    return render(request, "auth/register.html", context)
