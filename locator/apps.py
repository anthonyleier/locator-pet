from django.apps import AppConfig


class LocatorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'locator'

    def ready(self, *args, **kwargs):
        import locator.signals
        super_ready = super().ready()
        return super_ready
