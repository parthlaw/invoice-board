from django.shortcuts import render, redirect
# Create your views here.
from .forms import ShopForm


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
