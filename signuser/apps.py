from django.apps import AppConfig


class SignuserConfig(AppConfig):
    name = 'signuser'

    def ready(self):
        import signuser.signals
