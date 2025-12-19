from django.contrib import admin
from django.contrib import admin
from .models import Category, Product, Order, Profile
from django.contrib import admin
from .models import Product, Order
from django.contrib import admin
from .models import Order
# Register your models here.


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Profile)


#@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'status', 'created_at')
    list_filter = ('status',)




 