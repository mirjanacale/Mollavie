from django.db import models
from .category import Category
from cloudinary.models import CloudinaryField


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = CloudinaryField(
        'image',
        transformation=[
            {'width': 600, 'height': 400, 'crop': 'fill', 'quality': 'auto'}
        ]
     )
    created_at = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
