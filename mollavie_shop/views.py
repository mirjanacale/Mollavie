from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from django.urls import reverse

import stripe

from .forms import SignUpForm
from .models import Product
from .models.order import Order, OrderItem


# ───────────────────────────────────────────────────────────
#  General pages
# ───────────────────────────────────────────────────────────
def home(request):
    return render(request, "shop/index.html")


def signup_view(request):
    """Simple email + password registration."""
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = SignUpForm()
    return render(request, "shop/signup.html", {"form": form})


def gallery_view(request):
    artworks = Product.objects.all().order_by("-created_at")
    return render(request, "shop/gallery.html", {"artworks": artworks})


def artwork_detail_view(request, artwork_id):
    artwork = get_object_or_404(Product, id=artwork_id)
    return render(request, "shop/artwork_detail.html", {"artwork": artwork})


# ───────────────────────────────────────────────────────────
#  Stripe Checkout integration
# ───────────────────────────────────────────────────────────
stripe.api_key = settings.STRIPE_SECRET_KEY


def create_checkout_session(request, artwork_id):
    """
    Create a Stripe Checkout Session for a single artwork
    and redirect the user to Stripe’s hosted payment page.
    Guest checkout is allowed; we store product ID in session.
    """
    artwork = get_object_or_404(Product, id=artwork_id)

    if request.method == "POST":
        request.session["last_product"] = artwork.id

        success_url = (
            request.build_absolute_uri(reverse("payment_success"))
            + "?session_id={CHECKOUT_SESSION_ID}"
        )
        cancel_url = request.build_absolute_uri(reverse("payment_cancel"))

        try:
            checkout_session = stripe.checkout.Session.create(
                mode="payment",
                payment_method_types=["card"],
                line_items=[
                    {
                        "price_data": {
                            "currency": "gbp",
                            "unit_amount": int(artwork.price * 100),
                            "product_data": {"name": artwork.name},
                        },
                        "quantity": 1,
                    }
                ],
                success_url=success_url,
                cancel_url=cancel_url,
            )
            return redirect(checkout_session.url, code=303)

        except Exception as e:
            messages.error(request, f"Stripe error: {e}")
            return redirect("artwork_detail", artwork_id=artwork_id)

    # fallback GET → detail page
    return redirect("artwork_detail", artwork_id=artwork_id)


# ───────────────────────────────────────────────────────────
#  Payment success & cancel
# ───────────────────────────────────────────────────────────
def payment_success(request):
    """
    • Reads last_product from session
    • Creates Order (+ OrderItem)
    • Works for logged-in and guest users
    """
    product_id = request.session.get("last_product")
    order = None

    if product_id:
        product = get_object_or_404(Product, id=product_id)

        customer = request.user if request.user.is_authenticated else None

        order = Order.objects.create(customer=customer, paid=True)

        OrderItem.objects.create(order=order, product=product, quantity=1)

        product.is_available = False
        product.save(update_fields=["is_available"])

        del request.session["last_product"]

        messages.success(
            request,
            "Thank you! Your order has been placed."
            if customer
            else "Thank you! Your order has been placed (guest checkout).",
        )
    else:
        messages.warning(
            request,
            "No product recorded in session — order not saved. "
            "If you were charged, please contact support.",
        )

    return render(request, "shop/payment_success.html", {"order": order})


def payment_cancel(request):
    return render(request, "shop/payment_cancel.html")


# ───────────────────────────────────────────────────────────
#  Cart (session-based)
# ───────────────────────────────────────────────────────────
def add_to_cart(request, artwork_id):
    cart = request.session.get("cart", [])
    if artwork_id not in cart:
        cart.append(artwork_id)
        request.session["cart"] = cart
        messages.success(request, "Artwork added to cart!")
    else:
        messages.info(request, "Artwork already in cart.")
    return redirect("gallery")


def view_cart(request):
    cart = request.session.get("cart", [])
    artworks = Product.objects.filter(id__in=cart)
    return render(request, "shop/cart.html", {"artworks": artworks})


def remove_from_cart(request, artwork_id):
    cart = request.session.get("cart", [])
    if artwork_id in cart:
        cart.remove(artwork_id)
        request.session["cart"] = cart
        messages.success(request, "Removed from cart.")
    return redirect("view_cart")


# ───────────────────────────────────────────────────────────
#  Order history
# ───────────────────────────────────────────────────────────
@login_required
def my_orders_view(request):
    orders = Order.objects.filter(customer=request.user).order_by("-created_at")
    return render(request, "shop/my_orders.html", {"orders": orders})