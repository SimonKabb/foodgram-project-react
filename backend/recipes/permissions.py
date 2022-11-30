from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user.is_authenticated
        return True

    def has_object_permission(self, request, view, obj):
        if request.method == 'PACH':
            return request.user == obj.author
        if request.method in SAFE_METHODS or request.user.is_superuser:
            return True
        return request.user == obj.author
