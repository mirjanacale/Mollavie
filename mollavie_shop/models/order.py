from django.db import models
from django.contrib.auth.models import User
from .product import Product

class Order(models.Model):
    """
    Stores a single customer order, including shipping address, phone, and status.
    """
    customer = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders",
        help_text="The user who placed the order."
    )
    created_at = models.DateTimeField(auto_now_add=True, help_text="Order creation date and time.")
    address = models.CharField(max_length=255, blank=False, help_text="Shipping address for the order.")
    phone = models.CharField(max_length=20, blank=False, help_text="Customer's phone number.")
    paid = models.BooleanField(default=False, help_text="Order payment status.")

    def __str__(self):
        username = self.customer.username if self.customer else "Guest"
        return f"Order #{self.id} by {username}"

    class Meta:
        ordering = ['-created_at']

class OrderItem(models.Model):
    """
    An item within a customer order.
    """
    order = models.ForeignKey(
        Order, related_name='items', on_delete=models.CASCADE,
        help_text="The order this item belongs to."
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        help_text="The product purchased."
    )
    quantity = models.PositiveIntegerField(default=1, help_text="Number of units ordered.")

    def __str__(self):
        return f"{self.quantity} × {self.product.name} (Order #{self.order.id})"
