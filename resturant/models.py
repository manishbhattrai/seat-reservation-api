from django.db import models


# Create your models here.

class Restaurant(models.Model):

    STATUS_CHOICES = [
        ('open', 'Open'),
        ('close', 'Close'),
    ]

    name = models.CharField(max_length=300, blank=False, null= False)
    location = models.CharField(max_length=200, blank= False, null= False)
    phone_number = models.CharField(max_length=14, null= True, blank= True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, null=False, blank=False, default='open')
    admin = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='restaurants', null=True)


    def __str__(self):
        return self.name
    

class Table(models.Model):

    restaurant = models.ForeignKey(Restaurant, on_delete= models.CASCADE, related_name='Tables')
    numbers = models.IntegerField()
    seats = models.IntegerField()
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return f" Table {self.numbers} of {self.restaurant.name}"



