# mollavie_shop/admin.py

from django.contrib import admin
from .models import Category, Product, CustomerProfile, Order, OrderItem

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "is_available", "created_at", "category_list")
    list_editable = ("is_available",)
    list_filter = ("is_available", "categories")
    search_fields = ("name",)
    ordering = ("-created_at",)

    def category_list(self, obj):
        return ", ".join(c.name for c in obj.categories.all())
    category_list.short_description = "Categories"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(CustomerProfile)
admin.site.register(Order)
admin.site.register(OrderItem)
