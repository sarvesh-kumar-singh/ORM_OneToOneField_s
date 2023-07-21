from django.apps import AppConfig


class OneToOneConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'one_to_one'
    def ready(self):
        import one_to_one.signals
        
