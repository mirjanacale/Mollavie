from django.apps import AppConfig

class MollavieShopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mollavie_shop'

    def ready(self):
        import mollavie_shop.signals  # ✅ connects the signal
