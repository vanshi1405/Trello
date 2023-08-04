
from rest_framework.permissions import BasePermission

from trello1.models import Profile

#
# class CustomPermissions(BasePermission):
#     def has_permission(self, request, view):
#         if request.user:
#             user = request.user
#             user_obj=Profile.objects.get(user_id=user.id)
#             board = user_obj.board.all()
#             organization=board[0].organization
#             return True
#         return False
