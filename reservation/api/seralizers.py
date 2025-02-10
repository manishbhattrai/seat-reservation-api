from rest_framework import serializers
from reservation.models import Reservation
from user.models import User
from resturant.models import Table,Restaurant
from datetime import timedelta
from reservation.services import *



class ReservationSerializer(serializers.ModelSerializer):

    table_no = serializers.PrimaryKeyRelatedField(queryset = Table.objects.all(), many = True)
    restaurant_name = serializers.CharField(write_only =True)
    customer = serializers.CharField(source = 'customer.username', read_only = True)

    class Meta:
        model = Reservation
        fields = ['id','customer','table_no','date','is_completed','restaurant_name']

        def validate(self, data):

            tables = data.get('table_no')
            date = data.get('date')
            

            if not ReservationService.check_table_availability(tables, date):
             raise serializers.ValidationError("One or more tables are already reserved at the requested time.")
        
            return data
        
        def create(self, validated_data):
           
           restaurant_name = validated_data.pop('restaurant_name')


           try:
              restaurant = Restaurant.objects.get(name = restaurant_name)
            
           except Restaurant.DoesNotExist:
              raise serializers.ValidationError("Restaurant doesnot exists.")
           
           customer = self.context['request'].user
           
           reservation = ReservationService.create_reservation(
            restaurant=restaurant,
            tables=validated_data.get('table_no'),
            date=validated_data.get('date'),
            customer=customer
        )
        

           return reservation
           



