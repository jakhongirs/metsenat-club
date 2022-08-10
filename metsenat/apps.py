from django.apps import AppConfig


class MetsenatConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "metsenat"

    def ready(self):
        import metsenat.signals
