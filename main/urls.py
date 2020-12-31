from django.urls import path, include
from . import views

app_name = "main"


urlpatterns = [
    path('', views.main, name='main'),
    path('addShop/', views.index, name='addShop'),
    path('profile/', views.profile, name='profile'),
    path('change_password/', views.change_password, name='change_password'),

]
