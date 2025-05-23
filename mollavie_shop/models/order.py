from django.db import models
from django.contrib.auth.models import User
from .product import Product


class Order(models.Model):
    customer = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        username = self.customer.username if self.customer else "Guest"
        return f"Order {self.id} by {username}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"
