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
from .forms import CheckoutForm
import stripe

from .forms import SignUpForm, UserUpdateForm, CustomerProfileForm
from .models import Product, CustomerProfile
from .models.order import Order, OrderItem
from .models import Product, Category
from django.contrib.auth.decorators import user_passes_test
from .forms import ProductForm, CategoryForm
from .models.category import Category
from .models.product import Product

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
            messages.success(request, "Your account was created successfully! Welcome to Mollavie.")
            return redirect("shop:home")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = SignUpForm()
    return render(request, "shop/signup.html", {"form": form})


def gallery_view(request):
    category_id = request.GET.get("category")
    query = request.GET.get("q")  # new: search term
    sort = request.GET.get("sort")  # new: sort parameter

    artworks = Product.objects.all()

    if category_id:
        artworks = artworks.filter(category_id=category_id)

    if query:
        artworks = artworks.filter(name__icontains=query)

    # Apply sorting; default is newest first
    if sort == "price_asc":
        artworks = artworks.order_by("price")
    elif sort == "price_desc":
        artworks = artworks.order_by("-price")
    else:
        artworks = artworks.order_by("-created_at")
    categories = Category.objects.all().order_by("name")
    return render(request, "shop/gallery.html", {
        "artworks": artworks,
        "categories": categories,
    })


def artwork_detail_view(request, artwork_id):
    artwork = get_object_or_404(Product, id=artwork_id)
    return render(request, "shop/artwork_detail.html", {"artwork": artwork})


@login_required
def create_checkout_session(request, artwork_id):
    artwork = get_object_or_404(Product, id=artwork_id)

    #  1) Check availability!
    if not artwork.is_available:
        messages.error(request, "Sorry, this artwork has already been sold.")
        return redirect("shop:gallery")

    if request.method == "POST":
        #  2) Lock it immediately
        artwork.is_available = False
        artwork.save()

        #  3) Create an Order and OrderItem
        order = Order.objects.create(
            customer=request.user,
            address="Direct purchase - N/A",
            phone="N/A",
            paid=False
        )
        OrderItem.objects.create(
            order=order,
            product=artwork,
            quantity=1
        )

        #  4) Create the Stripe session
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
                reverse_lazy("shop:payment_cancel")
            ),
        )

        #  5) Store the session ID on your Order
        order.stripe_session_id = checkout_session.id
        order.save()
        request.session["order_id"] = order.id

        return redirect(checkout_session.url, code=303)

    return redirect("shop:artwork_detail", artwork_id=artwork_id)


def payment_success(request):
    order_id = request.session.pop("order_id", None)
    stripe_session_id = request.GET.get("session_id")
    order = None

    if order_id:
        order = get_object_or_404(Order, id=order_id)
    elif stripe_session_id:
        try:
            order = Order.objects.get(stripe_session_id=stripe_session_id)
        except Order.DoesNotExist:
            order = None

    if order:
        order.paid = True
        order.save()

        for item in order.items.all():
            item.product.is_available = False
            item.product.save()

        request.session["cart"] = {}
        messages.success(request, "Thank you! Your order has been placed.")
        total = sum(item.product.price * item.quantity for item in order.items.all())
    else:
        messages.warning(
            request,
            "No order recorded in session — order not saved. If you were charged, please contact support."
        )
        total = 0

    return render(request, "shop/payment_success.html", {"order": order, "total": total})

# mollavie_shop/views.py


def payment_cancel(request):
    order_id = request.session.get("order_id")
    if order_id:
        order = get_object_or_404(Order, id=order_id)
        if not order.paid:
            # return stock to the product(s)
            for item in order.items.all():
                item.product.is_available = True
                item.product.save()
            # delete unpaid order and its items
            order.delete()
        # clean up session
        request.session.pop("order_id", None)

    messages.info(request, "Payment was cancelled. The item is back in the store.")
    return render(request, "shop/payment_cancel.html")


def add_to_cart(request, artwork_id):
    product = get_object_or_404(Product, id=artwork_id)

    if not product.is_available:
        messages.error(request, "Sorry, this artwork is sold out and can't be added.")
        return redirect(reverse_lazy("shop:gallery"))

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


@login_required
def delete_profile(request):
    if request.method == "POST":
        user = request.user
        user.delete()
        messages.success(request, "Your account has been deleted.")
        return redirect("shop:home")
    return render(request, "shop/delete_profile_confirm.html")


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


@login_required
def checkout_view(request):
    cart = request.session.get("cart", {})
    if not cart:
        messages.error(request, "Your cart is empty.")
        return redirect("shop:view_cart")

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

    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user
            order.paid = False  # Payment will be marked after Stripe callback
            order.save()
            # Add items to order
            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    quantity=item["quantity"]
                )
            request.session["order_id"] = order.id  # store order for payment success
            return redirect("shop:start_payment")  # We'll add this Stripe view next!
    else:
        form = CheckoutForm()
    return render(request, "shop/checkout.html", {
        "form": form,
        "cart_items": cart_items,
        "total": total,
    })


@login_required
def start_payment(request):
    order_id = request.session.get("order_id")
    if not order_id:
        messages.error(request, "Order not found.")
        return redirect("shop:checkout")
    order = get_object_or_404(Order, id=order_id, customer=request.user)
    line_items = []
    for item in order.items.all():
        line_items.append({
            "price_data": {
                "currency": "eur",
                "unit_amount": int(item.product.price * 100),
                "product_data": {"name": item.product.name}
            },
            "quantity": item.quantity,
        })
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=line_items,
        mode="payment",
        success_url=request.build_absolute_uri(
            reverse_lazy("shop:payment_success") +
            "?session_id={CHECKOUT_SESSION_ID}"),
        cancel_url=request.build_absolute_uri(
            reverse_lazy("shop:payment_cancel")),
    )
    order.stripe_session_id = session.id
    order.save()

    return redirect(session.url, code=303)


@user_passes_test(lambda u: u.is_staff)
def admin_dashboard(request):
    """Display products & categories with add forms."""
    products = Product.objects.all().order_by('-created_at')
    categories = Category.objects.all().order_by('name')

    if request.method == 'POST':
        if 'add_product' in request.POST:
            p_form = ProductForm(request.POST, request.FILES)
            if p_form.is_valid():
                p_form.save()
                messages.success(request, "Product created successfully.")
                return redirect('shop:admin_dashboard')
        elif 'add_category' in request.POST:
            c_form = CategoryForm(request.POST)
            if c_form.is_valid():
                c_form.save()
                messages.success(request, "Category created successfully.")
                return redirect('shop:admin_dashboard')
    else:
        p_form = ProductForm()
        c_form = CategoryForm()

    return render(request, 'shop/admin_dashboard.html', {
        'products': products,
        'categories': categories,
        'product_form': p_form,
        'category_form': c_form,
    })


@user_passes_test(lambda u: u.is_staff)
def admin_delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    messages.success(request, "Product deleted.")
    return redirect('shop:admin_dashboard')


@user_passes_test(lambda u: u.is_staff)
def admin_delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    messages.success(request, "Category deleted.")
    return redirect('shop:admin_dashboard')


@user_passes_test(lambda u: u.is_staff)
def admin_edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product updated.")
            return redirect('shop:admin_dashboard')
    else:
        form = ProductForm(instance=product)
    return render(request, 'shop/admin_edit_product.html', {'form': form, 'product': product})


@user_passes_test(lambda u: u.is_staff)
def admin_edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "Category updated.")
            return redirect('shop:admin_dashboard')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'shop/admin_edit_category.html', {'form': form, 'category': category})

