# mollavie_shop/admin.py

from django.contrib import admin
from .models import Category, Product, CustomerProfile, Order, OrderItem


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "is_available", "created_at")
    list_editable = ("is_available",)
    list_filter = ("is_available",)
    search_fields = ("name",)
    ordering = ("-created_at",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(CustomerProfile)
admin.site.register(Order)
admin.site.register(OrderItem)
