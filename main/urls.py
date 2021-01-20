from django.urls import path, include
from . import views

app_name = "main"


urlpatterns = [
    path('', views.main, name='main'),
    path('addShop/', views.index, name='addShop'),
    path('profile/', views.profile, name='profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('addStock/', views.addStock, name='addStock'),
    path('addItem/', views.addItem, name='addItem'),
    path('invoice/', views.createInvoice, name="invoice"),
    path('test/', views.test, name='test'),
    path("search/", views.search, name="search")
]
