from django.apps import AppConfig
from django.contrib import admin

# from .models import Sleep


class TrackingConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tracking"

    def ready(self):
        # 必要であればここでmodelsをインポート
        from .models import Sleep

        admin.site.register(Sleep)
