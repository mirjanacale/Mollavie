import os
from pathlib import Path

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap

from mollavie_shop.sitemaps import StaticViewSitemap, ProductSitemap

BASE_DIR = Path(__file__).resolve().parent.parent

# Define your sitemaps
sitemaps = {
    'static': StaticViewSitemap,
    'products': ProductSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),

    # Mount all shop views (home, signup, login, gallery, profile, etc.)
    path('', include('mollavie_shop.urls', namespace='shop')),

    # Sitemap
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]

# Serve static files in development
urlpatterns += static(
    settings.STATIC_URL,
    document_root=BASE_DIR / 'mollavie_shop' / 'static'
)
