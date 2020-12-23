from django.shortcuts import render, redirect
from .signup import NewUserForm
from django.contrib.auth import login
from django.contrib import messages  # import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/login")
    else:
        form = NewUserForm()
    return render(request, "registration/register.html", {"form": form})


def login_request(request):
    return render(request, "registration/login.html", {"form": form})


def home(request):
    return render(request, "registration/test.html")
