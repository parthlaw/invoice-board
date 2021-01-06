from django.contrib import admin
from .models import Shop,item
from .models import Profile


# Register your models here.
admin.site.register(Shop)
admin.site.register(Profile)
admin.site.register(item)