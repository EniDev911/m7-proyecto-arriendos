from django.apps import AppConfig


class ArriendaYaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'arrienda_ya'

    def ready(self):
        import arrienda_ya.signal
