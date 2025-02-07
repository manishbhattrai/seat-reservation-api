from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import AdminRestaurantViewSet, TableViewSet


router = DefaultRouter()
router.register(r'restaurants', AdminRestaurantViewSet)
router.register(r'tables', TableViewSet, basename="table")



urlpatterns = [

    path('', include(router.urls)),

]