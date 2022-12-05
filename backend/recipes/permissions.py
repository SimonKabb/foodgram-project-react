from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user.is_authenticated
        return request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        if request.path[-5:] == 'edit/' or request.path[-5:] == '/edit':
            return False
        if (request.method in SAFE_METHODS or request.user.is_superuser):
            return True
        return request.user == obj.author
