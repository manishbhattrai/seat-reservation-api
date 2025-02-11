from rest_framework.views import APIView
from .seralizers import ReservationSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, viewsets
from rest_framework.decorators import action
from reservation.models import Reservation
from reservation.services import *
from rest_framework.exceptions import ValidationError
from .permissions import IsRestaurantAdmin



class ReservationViewSets(viewsets.ModelViewSet):

    queryset = Reservation.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ReservationSerializer



    def perform_create(self, serializer):

        try:
            customer = self.request.user
            tables = serializer.validated_data['table_no']
            date = serializer.validated_data['date']
            restaurant_name = serializer.validated_data['restaurant_name']

            reservation = ReservationService.create_reservation(
                restaurant_name, customer, tables, date
            )

            serializer.save(customer=customer, date=date, restaurant=reservation.restaurant)

        except ValueError as e:
           raise ValidationError(str(e))
        
        except Exception as e:  
            return Response({"error": "Internal Server Error", "details": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



    @action(detail=True, methods=['post'], url_path='complete', permission_classes = [IsRestaurantAdmin])
    def mark_as_completed(self, request, pk=None):
        
        reservation = self.get_object()
        ReservationService.mark_as_completed(reservation)

        return Response({"message": "Reservation marked as completed."}, status=status.HTTP_200_OK)
    

class ReservationView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        
        customer = self.request.user
        reservation = ReservationService.get_customer_reservation(customer=customer)
        serializer = ReservationSerializer(reservation, many = True)
        return Response(serializer.data)
    
