
from django.contrib import admin
from django.urls import path, include
from mollavie_shop import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mollavie_shop.urls')),
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('login/', auth_views.LoginView.as_view(template_name='shop/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
] + static(settings.STATIC_URL, document_root=BASE_DIR / 'mollavie_shop' / 'static')
