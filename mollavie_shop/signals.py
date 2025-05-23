from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models.customer import CustomerProfile


@receiver(post_save, sender=User)
def create_customer_profile(sender, instance, created, **kwargs):
    if created:
        CustomerProfile.objects.create(user=instance)
