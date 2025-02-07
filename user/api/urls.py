from django.urls import path
from .views import UserRegistrationView,UserLoginView,AdminRegistrationView


urlpatterns = [

    path('register/customer/', UserRegistrationView.as_view(), name= 'customer-register'),
    path('register/admin/', AdminRegistrationView.as_view(), name='admin-register'),
    path('login/',UserLoginView.as_view(), name='login'),  
   

]