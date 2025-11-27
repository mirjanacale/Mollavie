# mollavie_shop/sitemaps.py

from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Product


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = "weekly"

    def items(self):
        # Use the namespaced URL names defined in urls.py
        return ['shop:home', 'shop:gallery']

    def location(self, item):
        return reverse(item)


class ProductSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        # Filter on the existing field name
        return Product.objects.filter(is_available=True)

    def lastmod(self, obj):
        return obj.created_at
    
    
    def location(self, obj):
        return reverse('shop:artwork_detail', args=[obj.id])

