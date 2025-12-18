from django.contrib import admin
from django.contrib import admin
from .models import Category, Product, Order, Profile
from django.contrib import admin
from .models import Product, Order
# Register your models here.


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Profile)




