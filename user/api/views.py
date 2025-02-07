from rest_framework.views import APIView
from .serializers import CustomerRegistrationSerializer,UserLoginSerializer,RestaurantAdminSerializer
from rest_framework.response import Response
from rest_framework import status,generics
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from user.models import User
from .permissions import IsSuperAdmin


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CustomerRegistrationSerializer
    permission_classes = [AllowAny]



class AdminRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RestaurantAdminSerializer
    permission_classes = [IsSuperAdmin]



class UserLoginView(APIView):

    def post(self, request):

        data = request.data
        serializer = UserLoginSerializer(data = data)
        
        if serializer.is_valid():

            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username = username, password = password)

            if user:
                refresh = RefreshToken.for_user(user)
                return Response({

                    'refresh' : str(refresh),
                    'access' : str(refresh.access_token),

                 }, status= status.HTTP_200_OK)
            return Response({'error': 'Invalid credentials'}, status= status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST) 

