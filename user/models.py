from django.db import models
from django.contrib.auth.models import AbstractUser
from resturant.models import Restaurant

# Create your models here.

class User(AbstractUser):

    is_restaurant_admin = models.BooleanField(default= False)
    is_customer = models.BooleanField(default= True)
    restaurant = models.ForeignKey(Restaurant, on_delete= models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username


