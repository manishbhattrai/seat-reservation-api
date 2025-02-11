from rest_framework import permissions

class IsRestaurantAdmin(permissions.BasePermission):

    def has_permission(self, request, view):

        if not request.user.is_authenticated:

            return False
        
        
        if not hasattr(request.user, 'restaurant'):

            return False
        
        return True
    
    def has_object_permission(self, request, view, obj):

        if obj.restaurant.admin == request.user:

            return True
        
        return False
           
