from rest_framework import permissions


# class BlacklistPermission(permissions.BasePermission):
#     def has_permission(self, request, view):
#         id_addr=request.META['REMOTE_ADDR']
#         blacklisted = Blacklist.objects.filter(ip_addr=id_addr).exists()
#         return not blacklisted

class AnonPermissionOnly(permissions.BasePermission):
    message = 'You don\'t have permission for this action'

    # Non authenticated users only
    def has_permission(self, request, view):
        return not request.user.is_authenticated


class IsOwnerOrReadOnly(permissions.BasePermission):
    message = 'You must be the owner of the data'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
