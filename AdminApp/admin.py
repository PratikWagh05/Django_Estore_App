from django.contrib import admin
from .models import Category,Product,PaymentMaster
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display= ("id","category_name")

class Product_Admin(admin.ModelAdmin):
    list_display= ("id", "pname", "price","description","quantity","image","cat")

class PaymentMasterAdmin(admin.ModelAdmin):
    list_display = ("cardno", "cvv", "expiry", "balance")

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, Product_Admin)
admin.site.register(PaymentMaster, PaymentMasterAdmin)
