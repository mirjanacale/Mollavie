from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.decorators.http import require_POST
from .models import NewsletterSubscriber

import stripe

from .forms import SignUpForm, UserUpdateForm, CustomerProfileForm
from .models import Product, CustomerProfile
from .models.order import Order, OrderItem

stripe.api_key = settings.STRIPE_SECRET_KEY


def home(request):
    featured_products = (
        Product.objects.filter(is_available=True)
        .order_by('-created_at')[:4]
    )
    return render(
        request,
        "shop/index.html",
        {"featured_products": featured_products}
    )


def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("shop:home")
    else:
        form = SignUpForm()
    return render(request, "shop/signup.html", {"form": form})


def gallery_view(request):
    artworks = Product.objects.all().order_by("-created_at")
    return render(request, "shop/gallery.html", {"artworks": artworks})


def artwork_detail_view(request, artwork_id):
    artwork = get_object_or_404(Product, id=artwork_id)
    return render(request, "shop/artwork_detail.html", {"artwork": artwork})


def create_checkout_session(request, artwork_id):
    artwork = get_object_or_404(Product, id=artwork_id)
    if request.method == "POST":
        request.session["last_product"] = artwork.id
        try:
            checkout_session = stripe.checkout.Session.create(
                mode="payment",
                payment_method_types=["card"],
                line_items=[{
                    "price_data": {
                        "currency": "eur",
                        "unit_amount": int(artwork.price * 100),
                        "product_data": {"name": artwork.name},
                    },
                    "quantity": 1,
                }],
                success_url=request.build_absolute_uri(
                    reverse_lazy("shop:payment_success") +
                    "?session_id={CHECKOUT_SESSION_ID}"
                ),
                cancel_url=request.build_absolute_uri(
                    reverse_lazy("shop:payment_cancel")),
            )
            return redirect(checkout_session.url, code=303)
        except Exception as e:
            messages.error(request, f"Stripe error: {e}")
            return redirect("shop:artwork_detail", artwork_id=artwork_id)
    return redirect("shop:artwork_detail", artwork_id=artwork_id)


def payment_success(request):
    product_id = request.session.pop("last_product", None)
    order = None
    if product_id:
        product = get_object_or_404(Product, id=product_id)
        customer = request.user if request.user.is_authenticated else None
        order = Order.objects.create(customer=customer, paid=True)
        OrderItem.objects.create(order=order, product=product, quantity=1)
        product.is_available = False
        product.save(update_fields=["is_available"])
        messages.success(
            request,
            "Thank you! Your order has been placed."
            if customer
            else "Thank you! Your order has been placed (guest checkout)."
        )
    else:
        messages.warning(
            request,
            "No product recorded in session — order not saved. "
            "If you were charged, please contact support."
        )
    return render(request, "shop/payment_success.html", {"order": order})


def payment_cancel(request):
    return render(request, "shop/payment_cancel.html")


def add_to_cart(request, artwork_id):
    cart = request.session.get("cart", {})
    key = str(artwork_id)
    if key in cart:
        cart[key] += 1
        messages.info(request, "Increased quantity.")
    else:
        cart[key] = 1
        messages.success(request, "Artwork added to cart!")
    request.session["cart"] = cart
    return redirect(reverse_lazy("shop:gallery"))


def view_cart(request):
    cart = request.session.get("cart", {})
    cart_items = []
    for pid, qty in cart.items():
        try:
            p = Product.objects.get(id=pid)
            cart_items.append({
                "product": p,
                "quantity": qty,
                "subtotal": p.price * qty
            })
        except Product.DoesNotExist:
            continue
    total = sum(item["subtotal"] for item in cart_items)
    return render(
        request, "shop/cart.html",
        {"cart_items": cart_items, "total": total}
    )


@require_POST
def update_cart(request, artwork_id):
    cart = request.session.get("cart", {})
    key, qty = str(artwork_id), int(request.POST.get("quantity", 1))
    if qty > 0:
        cart[key] = qty
        messages.success(request, "Quantity updated.")
    else:
        cart.pop(key, None)
        messages.info(request, "Item removed.")
    request.session["cart"] = cart
    return redirect(reverse_lazy("shop:view_cart"))


def remove_from_cart(request, artwork_id):
    cart = request.session.get("cart", {})
    cart.pop(str(artwork_id), None)
    request.session["cart"] = cart
    messages.success(request, "Removed from cart.")
    return redirect(reverse_lazy("shop:view_cart"))


def clear_cart(request):
    request.session["cart"] = {}
    messages.success(request, "Cart cleared.")
    return redirect(reverse_lazy("shop:view_cart"))


@login_required
def checkout_cart_view(request):
    cart = request.session.get("cart", {})
    if not cart:
        messages.error(request, "Your cart is empty.")
        return redirect(reverse_lazy("shop:view_cart"))
    items = []
    for pid, qty in cart.items():
        try:
            p = Product.objects.get(id=pid)
            items.append({
                "price_data": {
                    "currency": "eur",
                    "unit_amount": int(p.price * 100),
                    "product_data": {"name": p.name}
                },
                "quantity": qty,
            })
        except Product.DoesNotExist:
            continue
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=items,
        mode="payment",
        success_url=request.build_absolute_uri(
            reverse_lazy("shop:payment_success")),
        cancel_url=request.build_absolute_uri(
            reverse_lazy("shop:payment_cancel")),
    )
    return redirect(session.url, code=303)


@login_required
def my_orders_view(request):
    profile, _ = CustomerProfile.objects.get_or_create(user=request.user)
    orders = Order.objects.filter(
        customer=request.user).order_by("-created_at")
    return render(request, "shop/my_orders.html",
                  {"profile": profile, "orders": orders})


@login_required
def profile_view(request):
    profile, _ = CustomerProfile.objects.get_or_create(user=request.user)
    orders = Order.objects.filter(customer=request.user)
    return render(request, "shop/profile.html",
                  {"profile": profile, "orders": orders})


@login_required
def edit_profile(request):
    user = request.user
    profile = user.customerprofile
    if request.method == "POST":
        uf = UserUpdateForm(request.POST, instance=user)
        pf = CustomerProfileForm(request.POST, instance=profile)
        if uf.is_valid() and pf.is_valid():
            uf.save()
            pf.save()
            return redirect("shop:profile")
    else:
        uf = UserUpdateForm(instance=user)
        pf = CustomerProfileForm(instance=profile)
    return render(request, "shop/edit_profile.html",
                  {"user_form": uf, "profile_form": pf})


def subscribe(request):
    if request.method == "POST":
        email = request.POST.get("email")
        if email:
            # Prevent duplicate subscriptions
            if not NewsletterSubscriber.objects.filter(email=email).exists():
                NewsletterSubscriber.objects.create(email=email)
                messages.success(request, "Thank you for subscribing!")
            else:
                messages.info(request, "You're already subscribed.")
    return redirect("shop:home")
