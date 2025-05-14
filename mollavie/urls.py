
from django.contrib import admin
from django.urls import path
from mollavie_shop import views
from django.conf import settings
from django.conf.urls.static import static
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('gallery/', views.gallery_view, name='gallery'),                                                                                  # Admin panel

] + static(settings.STATIC_URL, document_root=BASE_DIR / 'mollavie_shop' / 'static')
