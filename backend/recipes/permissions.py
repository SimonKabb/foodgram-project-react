from rest_framework.permissions import BasePermission, SAFE_METHODS


# class IsOwnerOrAdminOrReadOnly(BasePermission):
#     def has_permission(self, request, view):
#         if request.method == 'POST':
#             return request.user.is_authenticated
#         return request.method in SAFE_METHODS

#     def has_object_permission(self, request, view, obj):
#         if request.META['HTTP_REFERER'][-5:] == 'edit/' and request.user != obj.author:
#             return False
#         elif request.method in SAFE_METHODS or request.user.is_superuser:
#             return True
#         else:
#             return True
class IsOwnerOrAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user.is_authenticated
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS or request.user.is_superuser:
            return True
        return request.user == obj.author
