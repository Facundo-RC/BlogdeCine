from django.apps import AppConfig


class UsuariosConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "usuarios"

    def ready(self):
        # Registra la señal que crea el perfil al crear un usuario.
        from . import signals  # noqa: F401
