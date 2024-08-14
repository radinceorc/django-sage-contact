from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SageContactConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "sage_contact"
    verbose_name = _("Sage Contact")

    def ready(self) -> None:
        import sage_contact.settings.check
        import sage_contact.signals
