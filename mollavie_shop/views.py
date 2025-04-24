import stripe
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login, authenticate


stripe.api_key = settings.STRIPE_SECRET_KEY


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


def create_checkout_session(request, artwork_id):
    artwork = get_object_or_404(Product, id=artwork_id)

    if request.method == "POST":
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'gbp',
                    'unit_amount': int(artwork.price * 100),  # Stripe uses pence
                    'product_data': {
                        'name': artwork.title,
                    },
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri('/') + '?success=true',
            cancel_url=request.build_absolute_uri('/') + '?cancel=true',
        )
        return redirect(checkout_session.url)

