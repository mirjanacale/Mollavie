import stripe
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from .models.order import Order, OrderItem
from .models import Product
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth import login, authenticate


def home(request):
    return render(request, 'shop/index.html')

     
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'shop/signup.html', {'form': form})


def gallery_view(request):
    artworks = Product.objects.all().order_by('-created_at')
    return render(request, 'shop/gallery.html', {'artworks': artworks})


def artwork_detail_view(request, artwork_id):
    artwork = get_object_or_404(Product, id=artwork_id)
    return render(request, 'shop/artwork_detail.html', {'artwork': artwork})


from django.http import JsonResponse

stripe.api_key = settings.STRIPE_SECRET_KEY


def create_checkout_session(request, artwork_id):
    artwork = get_object_or_404(Product, id=artwork_id)

    if request.method == "POST":
        request.session['last_product'] = artwork.id
        try:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'gbp',
                        'unit_amount': int(artwork.price * 100),
                        'product_data': {
                            'name': artwork.name,
                        },
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url=request.build_absolute_uri('/success/'),
                cancel_url=request.build_absolute_uri('/cancel/'),
            )
            return redirect(checkout_session.url)
        except Exception as e:
            messages.error(request, f"Stripe error: {str(e)}")
            return redirect('artwork_detail', artwork_id=artwork_id)
    else:
        return redirect('artwork_detail', artwork_id=artwork_id)


def payment_success(request):
    product_id = request.session.get('last_product')

    if product_id:
        product = get_object_or_404(Product, id=product_id)

        # Create order
        order = Order.objects.create(
            customer=request.user,
            paid=True,
        )

        # Create order item
        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=1,
        )

        # Mark product as sold
        product.is_available = False
        product.save()

        # Clear session
        del request.session['last_product']

        messages.success(request, f"Thank you, {request.user.username}! Your order has been placed.")

    else:
        messages.warning(request, "No product was recorded in session. Order not saved.")

    return render(request, 'shop/payment_success.html')

    
def payment_cancel(request):
    return render(request, 'shop/payment_cancel.html') 


# Add to cart
def add_to_cart(request, artwork_id):
    cart = request.session.get('cart', [])
    if artwork_id not in cart:
        cart.append(artwork_id)
        request.session['cart'] = cart
        messages.success(request, "Artwork added to cart!")
    else:
        messages.info(request, "Artwork already in cart.")
    return redirect('gallery')


#  View cart
def view_cart(request):
    cart = request.session.get('cart', [])
    artworks = Product.objects.filter(id__in=cart)
    return render(request, 'shop/cart.html', {'artworks': artworks})


#  Remove from cart
def remove_from_cart(request, artwork_id):
    cart = request.session.get('cart', [])
    if artwork_id in cart:
        cart.remove(artwork_id)
        request.session['cart'] = cart
        messages.success(request, "Removed from cart.")
    return redirect('view_cart')

    


