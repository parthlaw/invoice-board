from django.shortcuts import render, redirect
# Create your views here.
from django.contrib import messages
from .forms import ShopForm,  ItemForm, InvoiceForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import JsonResponse, HttpResponse
from .models import stock, item
from django.db.models import Avg, Count
from django.views.decorators.csrf import csrf_exempt
import logging
logger = logging.getLogger('name')


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
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('/profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'main/change_password.html', {'form': form})


def addStock(request):
    form = StockForm()

    if request.user.is_authenticated:
        User = request.user
        if request.method == 'POST':
            form = StockForm(request.POST)
            if form.is_valid():
                form.save()

        return render(request, 'main/index.html', context={'form': form, "User": User})
    else:
        return redirect('/login')


def addItem(request):
    form = ItemForm()
    if request.user.is_authenticated:
        User = request.user
        if request.method == 'POST':
            form = ItemForm(request.POST)
            if form.is_valid():
                form.save()
        return render(request, 'main/index.html', context={'form': form, 'User': User, 'formType': """Add Item"""})
    else:
        return redirect('/login')


def createInvoice(request):
    form = InvoiceForm()
    if request.user.is_authenticated:
        User = request.user
        if request.method == 'POST':
            form = InvoiceForm(request.POST)
            if form.is_valid():
                form.save()
        return render(request, 'main/addStock.html', context={'form': form, 'User': User})
    else:
        return redirect('/login')


def test(request):
    itemData = item.objects.all()
    for i in itemData:
        stockData = stock.objects.all().filter(item_id=i.id)
        logger.info(stockData)
    return render(request, "main/createInvoice.html")


@csrf_exempt
def search(request):
    if request.method == "POST":
        import json
        post_data = json.loads(request.body.decode("utf-8"))
        obj = stock.objects.filter(item_id=1)
        logger.info(obj)
    son = {'message': 'I listned'}
    return JsonResponse(son)
