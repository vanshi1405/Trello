
from rest_framework.permissions import BasePermission

from trello1.models import Profile


class CustomOrganizationPermissions(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        p = Profile.objects.get(user_id=user.id)
        if view.action in ["list", "retrieve","create","update"] and p.user_type=="organization_admin":
            return True
        elif view.action in ["list"] and p.user_type=="organization_user":
            return True
        return False
