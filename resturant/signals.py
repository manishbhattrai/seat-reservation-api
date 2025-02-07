from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from user.models import User


@receiver(post_save, sender=User)

def admin_assign(sender, instance, created, **kwargs):

    if created:
        restaurant = instance.restaurant

        if restaurant:
            try:
                restaurant.admin = instance
                restaurant.save()
            
            except ObjectDoesNotExist:
                raise ValueError(f"{restaurant} doesnot exists.")