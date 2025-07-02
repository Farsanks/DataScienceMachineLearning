from django.apps import AppConfig

class DetectorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'detector'

    def ready(self):
        import detector.signals  # <-- Make sure this line is added
