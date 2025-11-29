from django.db import models
from .category import Category
from cloudinary.models import CloudinaryField
# mollavie_shop/models/product.py
from django.db import models
from .category import Category
from django.contrib.auth.models import User


class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="products"
    )
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = CloudinaryField('image')
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    favorites = models.ManyToManyField(User, related_name='favorite_products', blank=True)

    def __str__(self):
        return self.name
