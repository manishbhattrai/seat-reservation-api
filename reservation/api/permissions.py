from rest_framework import permissions

class IsRestaurantAdmin(permissions.BasePermission):

    def has_permission(self, request, view):

        if not request.user.is_authenticated:
            return False
        
        
        return hasattr(request.user, 'restaurant') and request.user == request.user.is_restaurant_admin
