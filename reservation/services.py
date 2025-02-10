from datetime import timedelta
from .models import Reservation
from django.utils import timezone
from resturant.models import Restaurant


class ReservationService:

    @staticmethod
    def check_table_availability(tables, date):
        conflicting_reservations = Reservation.objects.filter(
            table_no__in=tables,
            date__range=[date, date + timedelta(minutes=15)] 
        )
        if conflicting_reservations.exists():
            return False
        return True

    @staticmethod
    def create_reservation(restaurant_name, customer, tables, date):


          
        if Reservation.objects.filter(customer=customer, restaurant__name=restaurant_name, date=date).exists():
            raise ValueError(f"A reservation already exists.")
        
        if not ReservationService.check_table_availability(tables, date):
            raise ValueError("Tables are already reserved currently.")
        
        try:
            restaurant = Restaurant.objects.get(name=restaurant_name)
        except Restaurant.DoesNotExist:
            raise ValueError(f"Restaurant does not exist.")
        
        reservation = Reservation.objects.create(restaurant=restaurant, customer=customer, date=date)
        

        reservation.table_no.set(tables)
        for table in tables:
            table.is_available = False
            table.save()
        return reservation

    @staticmethod
    def mark_as_completed(reservation):

        reservation.is_completed = True
        reservation.save()
    
    @staticmethod
    def get_customer_reservation(customer):

        return Reservation.objects.filter(customer=customer).order_by('date')

    