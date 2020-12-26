from django.shortcuts import render, redirect
from .signup import NewUserForm
from django.contrib import messages  # import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/login")
    else:
        form = NewUserForm()
    return render(request, "registration/register.html", {"form": form})


def home(request):
    if request.user.is_authenticated:
        return render(request, "registration/test.html")
    else:
        return redirect('/login')
