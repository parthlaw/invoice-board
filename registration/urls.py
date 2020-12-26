from django.urls import path, include
from . import views

app_name = "registration"


urlpatterns = [

    path('register/', views.register_request, name='register'),
    path('test/', views.home, name="home"),
    path('', include("django.contrib.auth.urls")),
]
