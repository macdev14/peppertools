from rest_framework import permissions
from rest_framework_simplejwt.views import token_verify

from rest_framework.permissions import BasePermission,SAFE_METHODS

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if token_verify(request.methodheaders['Authorization']):
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user
    



class IsOwnerProfileOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        print(obj)
        if request.method in SAFE_METHODS:
            return True
        return obj.user==request.user