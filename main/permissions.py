from rest_framework.permissions import SAFE_METHODS, BasePermission

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_staff

class isAdminUser(BasePermission):
    def has_permission(self, request, view):

        return bool(request.user and request.user.is_admin)
class isClientUser(BasePermission):
    def has_permission(self, request, view):

        return bool(request.user and request.user.is_client)
