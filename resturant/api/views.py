from rest_framework import viewsets, permissions
from .serializers import ResturantSerializer, TableSerializer
from resturant.models import Restaurant, Table
from .permissions import IsAdminUserReadOnly, IsRestaurantAdminUserorReadOnly
from rest_framework.exceptions import PermissionDenied


class AdminRestaurantViewSet(viewsets.ModelViewSet):
    serializer_class = ResturantSerializer
    queryset = Restaurant.objects.all()
    permission_classes = [IsAdminUserReadOnly]


class TableViewSet(viewsets.ModelViewSet):
    serializer_class = TableSerializer
    permission_classes = [IsRestaurantAdminUserorReadOnly]

    
    def get_queryset(self):
        user = self.request.user
        restaurant_id = self.request.query_params.get('restaurant_id')  


        if user.is_authenticated and user.is_superuser:
            
            return Table.objects.all()

        if user.is_authenticated and getattr(user, 'is_restaurant_admin', False):
            if user.restaurant:
                
                return Table.objects.filter(restaurant=user.restaurant)
        
            return Table.objects.none()

        
        if restaurant_id:
            tables = Table.objects.filter(restaurant_id=restaurant_id, is_available=True)
            return tables

        return Table.objects.none()
   
         
    def get_permissions(self):

        if self.action in ['list', 'retrieve']:

            return [permissions.AllowAny()]
        
        return [IsRestaurantAdminUserorReadOnly()] 
    

    
    def perform_create(self, serializer):

        user = self.request.user
        
        restaurant = serializer.validated_data.get('restaurant')

        if user == restaurant.admin or user.is_superuser:

            serializer.save()
        
        else:
            raise PermissionDenied("You are not allowed to create a table for this restaurant.")
        

        
    
    def update(self, request, *args, **kwargs):

        user = self.request.user

        table = self.get_object()

        if user.is_superuser or (user.is_restaurant_admin and table.restaurant == user.restaurant):

            return super().update(request, *args, **kwargs)
        
        else:
            raise PermissionDenied('You are not allowed to update the table for this restaurant.')