from django.shortcuts import render, redirect
# Create your views here.
from django.contrib import messages
from .forms import ShopForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


def main(request):
    if request.user.is_authenticated:
        User = request.user
        return render(request, 'dashboard/dashboard.html', {"User": User})
    else:
        return redirect('/login')


def index(request):
    form = ShopForm()

    if request.user.is_authenticated:
        User = request.user
        if request.method == 'POST':
            form = ShopForm(request.POST)
            if form.is_valid():
                form.save()

        return render(request, 'main/index.html', context={'form': form, "User": User})
    else:
        return redirect('/login')

def profile(request):
    if request.user.is_authenticated:
        User = request.user
        return render(request, 'main/profile.html', {"User": User})
    else:
        return redirect('/login')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'main/change_password.html', {'form': form})
          
     
  


