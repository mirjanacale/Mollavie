import stripe
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse  # kept in case you later use Ajax
from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
)
from django.urls import reverse

from .forms import SignUpForm
from .models import Product
from .models.order import Order, OrderItem

# ────────────────────────────────────────────────────────────
#  General pages
# ────────────────────────────────────────────────────────────
def home(request):
    return render(request, "shop/index.html")


def signup_view(request):
    """User registration view."""
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


# ────────────────────────────────────────────────────────────
#  Stripe Checkout integration
# ────────────────────────────────────────────────────────────
stripe.api_key = settings.STRIPE_SECRET_KEY


def create_checkout_session(request, artwork_id):
    """
    Creates a Stripe Checkout Session for a single artwork
    and redirects the user to Stripe’s hosted payment page.
    """
    artwork = get_object_or_404(Product, id=artwork_id)

    if request.method == "POST":
        # Remember the product so we can create an Order on success.
        request.session["last_product"] = artwork.id

        # Build absolute success / cancel URLs that work on localhost *and* Heroku.
        success_url = (
            request.build_absolute_uri(reverse("payment_success"))
            + "?session_id={CHECKOUT_SESSION_ID}"
        )
        cancel_url = request.build_absolute_uri(reverse("payment_cancel"))

        try:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=["card"],
                line_items=[
                    {
                        "price_data": {
                            "currency": "gbp",
                            "unit_amount": int(artwork.price * 100),  # pence
                            "product_data": {"name": artwork.name},
                        },
                        "quantity": 1,
                    }
                ],
                mode="payment",
                success_url=success_url,
                cancel_url=cancel_url,
            )
            # Stripe recommends 303 on redirect to an external domain
            return redirect(checkout_session.url, code=303)

        except Exception as e:
            messages.error(request, f"Stripe error: {e}")
            return redirect("artwork_detail", artwork_id=artwork_id)

    # GET requests fall back to detail page
    return redirect("artwork_detail", artwork_id=artwork_id)


# ────────────────────────────────────────────────────────────
#  Payment result pages
# ────────────────────────────────────────────────────────────
def payment_success(request):
    """
    Reads the last product from the session, creates an Order + OrderItem,
    marks the product unavailable, and thanks the user.
    """
    product_id = request.session.get("last_product")
    order = None

    if product_id:
        product = get_object_or_404(Product, id=product_id)

        # Create order
        order = Order.objects.create(customer=request.user, paid=True)

        # Create order item
        OrderItem.objects.create(order=order, product=product, quantity=1)

        # Mark product as sold
        product.is_available = False
        product.save()

        del request.session["last_product"]
        messages.success(
            request, f"Thank you, {request.user.username}! Your order has been placed."
        )
    else:
        messages.warning(request, "No product was recorded in session. Order not saved.")

    return render(request, "shop/payment_success.html", {"order": order})


def payment_cancel(request):
    """Simple ‘payment cancelled’ page."""
    return render(request, "shop/payment_cancel.html")


# ────────────────────────────────────────────────────────────
#  Cart helpers (session-based)
# ────────────────────────────────────────────────────────────
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


# ────────────────────────────────────────────────────────────
#  Order history
# ────────────────────────────────────────────────────────────
@login_required
def my_orders_view(request):
    orders = Order.objects.filter(customer=request.user).order_by("-created_at")
    return render(request, "shop/my_orders.html", {"orders": orders})

