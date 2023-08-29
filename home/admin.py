from django.contrib import admin

# Register your models here.
from .models import Product, Expenses, Orders
admin.site.register(Product)
admin.site.register(Expenses)
admin.site.register(Orders)
