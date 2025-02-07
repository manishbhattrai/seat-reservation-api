from django.apps import AppConfig


class ResturantConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'resturant'

    def ready(self):

        print('my restaurant app is ready and working.')

        import resturant.signals
