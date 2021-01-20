from django.contrib import admin
from .models import Shop, Profile, stock, item


# Register your models here.
admin.site.register(Shop)
admin.site.register(Profile)
admin.site.register(stock)
admin.site.register(item)
