from rest_framework import permissions


class PermissionHelperMixin(object):
    def admin_editable_only(self):
        if self.action not in ['list', 'retrieve']:
            return [permissions.IsAdminUser()]
        else:
            return []

    def authenticated_user_editable_only(self):
        if self.action not in ['list', 'retrieve']:
            return [permissions.IsAuthenticated()]
        else:
            return []


class AuthPermission(object):
    pass


class AuthorAllStaffAllButEditOrReadOnly(permissions.BasePermission):
    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if request.method in permissions.SAFE_METHODS:
            return True

        if obj.author == request.user:
            return True

        if request.user.is_staff and request.method not in self.edit_methods:
            return True

        return False
