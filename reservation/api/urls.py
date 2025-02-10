from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ReservationViewSets, ReservationView


router = DefaultRouter()
router.register(r'reservations', ReservationViewSets, basename='reservation')

urlpatterns = [

    path('', include(router.urls)),
    path('my-reservations/', ReservationView.as_view(), name='my-reservations'),

]