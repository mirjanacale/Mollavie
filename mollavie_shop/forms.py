from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models.order import Order
from .models.customer import CustomerProfile  


# ---- Signup Form ----
class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


# ---- Profile Edit Forms ----
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile
        fields = ['phone', 'address']


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['address', 'phone']
        widgets = {
            'address': forms.TextInput(attrs={
                'placeholder': 'Enter delivery address',
                'class': 'form-control'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Enter your phone number',
                'class': 'form-control'
            }),
        }        
