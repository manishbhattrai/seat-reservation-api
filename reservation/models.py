from django.db import models
from resturant.models import Table,Restaurant

# Create your models here.

class Reservation(models.Model):

    customer = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='reservations')
    table_no = models.ManyToManyField(Table, related_name='reservations')
    date = models.DateTimeField(auto_now_add= False, auto_now= False)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='reservations', null=True)
    is_completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('customer', 'date', 'restaurant')


    def __str__(self):
        return f"reservation for {self.customer.username} at {self.restaurant} on {self.date}"
    

    


