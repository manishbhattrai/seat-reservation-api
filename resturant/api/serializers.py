from resturant.models import Restaurant, Table
from rest_framework import serializers


class ResturantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ['name','location','phone_number','status']


class TableSerializer(serializers.ModelSerializer):

    class Meta:
        model = Table
        fields = ['numbers','seats','is_available']