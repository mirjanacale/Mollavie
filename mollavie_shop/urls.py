from django.contrib import admin
from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from .views import subscribe
from . import views
from django.urls import path
app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='shop/login.html',
            redirect_authenticated_user=True,
            success_url=reverse_lazy('shop:gallery')
        ),
        name='login'
    ),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('artwork/<int:artwork_id>/', views.artwork_detail_view,
         name='artwork_detail'),
    path('buy/<int:artwork_id>/', views.create_checkout_session,
         name='create_checkout_session'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('success/', views.payment_success, name='payment_success'),
    path('cancel/', views.payment_cancel, name='payment_cancel'),

    # Cart
    path("cart/", views.view_cart, name="view_cart"),
    path("cart/add/<int:artwork_id>/", views.add_to_cart, name="add_to_cart"),
    path("cart/update/<int:artwork_id>/", views.update_cart,
         name="update_cart"),
    path("cart/remove/<int:artwork_id>/", views.remove_from_cart,
         name="remove_from_cart"),
    path("cart/clear/", views.clear_cart, name="clear_cart"),

    # Orders & Profile
    path('my-orders/',    views.my_orders_view, name='my_orders'),
    path('profile/',      views.profile_view,   name='profile'),
    path('profile/edit/', views.edit_profile,  name='edit_profile'),
    path("subscribe/", views.subscribe, name="subscribe"),
    path('start-payment/', views.start_payment, name='start_payment'),
    path('profile/delete/', views.delete_profile, name='delete_profile'),

    # … existing routes
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path(
        'admin-dashboard/product/<int:product_id>/edit/',
        views.admin_edit_product,
        name='admin_edit_product'
    ),
    path(
        'admin-dashboard/product/<int:product_id>/delete/',
        views.admin_delete_product,
        name='admin_delete_product'
    ),
    path(
        'admin-dashboard/category/<int:category_id>/edit/',
        views.admin_edit_category,
        name='admin_edit_category'
    ),
    path(
        'admin-dashboard/category/<int:category_id>/delete/',
        views.admin_delete_category,
        name='admin_delete_category'
    ),

    
    
    path('favorite/<int:artwork_id>/', views.toggle_favorite, name='toggle_favorite')
]
