from rest_framework import permissions


class IsRestaurantAdminUserorReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.restaurant.admin == request.user or request.user.is_superuser

class IsAdminUserReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return True
        
        if request.user and request.user.is_superuser:
            print("User is a superuser.")
            return True
        else:
            print("Permission denied.")
            return False
    

