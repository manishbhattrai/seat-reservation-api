from rest_framework import serializers
from user.models import User
from resturant.models import Restaurant

class CustomerRegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = ['username','email','password']


    def validate(self, data):
        if data.get('username') and not data.get('password'):
            raise serializers.ValidationError({"message": "Password is Required."})
        return data

    def create(self, validated_data):

        password = validated_data.pop('password')

        validated_data['is_customer'] = True
        validated_data['is_restaurant_admin'] = False
       
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        return user


class RestaurantAdminSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True)
    restaurant_name = serializers.CharField(write_only=True)  

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'restaurant_name']

    def validate(self, data):
        request = self.context.get('request')

        if not request.user.is_superuser:
            raise serializers.ValidationError({"error": "Only super admins can create restaurant admins."})

        return data

    def create(self, validated_data):
        password = validated_data.pop('password') 
        restaurant_name = validated_data.pop('restaurant_name', None) 

        try:
            restaurant = Restaurant.objects.get(name=restaurant_name)
        except Restaurant.DoesNotExist:
            raise serializers.ValidationError({"restaurant_name": "Invalid restaurant name."})


        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            is_restaurant_admin=True, 
            is_customer=False,  
            restaurant=restaurant  
        )

        user.set_password(password)
        user.save()

        return user
        
    
class UserLoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField(write_only = True)

    




