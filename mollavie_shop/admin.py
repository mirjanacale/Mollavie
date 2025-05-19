# mollavie_shop/admin.py
from django.contrib import admin
from .models import Category, Product, CustomerProfile, Order, OrderItem


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "is_available", "created_at", "category")
    list_editable = ("is_available",)       # ← inline checkbox
    list_filter = ("is_available", "category")
    search_fields = ("name",)
    ordering = ("-created_at",)


# keep simple registrations for the rest
admin.site.register(Category)
admin.site.register(CustomerProfile)
admin.site.register(Order)
admin.site.register(OrderItem)
