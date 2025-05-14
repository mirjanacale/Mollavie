"""
URL configuration for mollavie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
     path('', views.home, name='home'),
     path('signup/', views.signup_view, name='signup'),
     path('login/', auth_views.LoginView.as_view(template_name='shop/login.html'), name='login'),
     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
     path('gallery/', views.gallery_view, name='gallery'),
     path('artwork/<int:artwork_id>/', views.artwork_detail_view, name='artwork_detail'),
     path('buy/<int:artwork_id>/', views.create_checkout_session, name='create_checkout_session'),
     path('cart/', views.view_cart, name='view_cart'),
     path('cart/add/<int:artwork_id>/', views.add_to_cart, name='add_to_cart'),
     path('cart/remove/<int:artwork_id>/', views.remove_from_cart, name='remove_from_cart'),
     path('success/', views.payment_success, name='payment_success'),
     path('cancel/', views.payment_cancel, name='payment_cancel'),


]
