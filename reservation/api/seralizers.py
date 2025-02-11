from rest_framework import serializers
from reservation.models import Reservation
from user.models import User
from resturant.models import Table,Restaurant
from datetime import timedelta
from reservation.services import *



class ReservationSerializer(serializers.ModelSerializer):

    table_no = serializers.PrimaryKeyRelatedField(queryset = Table.objects.all(), many = True)
    restaurant_name = serializers.CharField(write_only = True)
    customer = serializers.CharField(source = 'customer.username', read_only = True)

    class Meta:
        model = Reservation
        fields = ['id','customer','table_no','date','is_completed','restaurant_name']

        def validate(self, data):

            tables = data.get('table_no')
            date = data.get('date')
            restaurant_name = data.get('restaurant_name')

            customer = self.context['request'].user
            

            if Reservation.objects.filter(customer=customer, restaurant__name=restaurant_name, date=date).exists():
             raise serializers.ValidationError("One or more tables are already reserved at the requested time.")
            
            if not ReservationService.check_table_availability(tables, date):
             raise serializers.ValidationError("One or more tables are already reserved at the requested time.")
        
            return data
        
    def create(self, validated_data):
        restaurant_name = validated_data.pop("restaurant_name", None)

        if not restaurant_name:
            raise serializers.ValidationError({"restaurant_name": "This field is required."})

    
        try:
            restaurant = Restaurant.objects.get(name=restaurant_name)
        except Restaurant.DoesNotExist:
            raise serializers.ValidationError({"restaurant_name": "Restaurant does not exist."})

        customer = self.context["request"].user
        date = validated_data.get("date")
        table_no = validated_data.get("table_no")

    
        reservation = ReservationService.create_reservation(
        restaurant=restaurant,
        tables=table_no,
        date=date,
        customer=customer,
        )

        return reservation

           



