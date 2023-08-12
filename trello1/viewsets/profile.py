# from rest_framework import viewsets
import trello1.serializers.profile
from trello1.custom.custommodelviewset import *
from trello1.custom.pagination import CustomPagination
from trello1.custom.custompermissions import *
from trello1.models import *



class ProfileViewset(CustomdeleteModelViewset,CustomProfileModelViewset):
    queryset = Profile.objects.all()
    serializer_class = trello1.serializers.profile.ProfileSerializer
    pagination_class = CustomPagination
    permission_classes = [CustomProfilePermissions]

    # def get_queryset(self):
    #     if self.action == 'retrieve':
    #         user = self.request.user
    #         pk = self.kwargs['pk']
    #         try:
    #             member_object = Profile.objects.get(user_id=user.id)
    #             queryset = member_object
    #             return queryset
    #         except NotFound:
    #             raise "user is not valid"
    #     return super().get_queryset()