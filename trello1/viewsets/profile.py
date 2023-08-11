# from rest_framework import viewsets
import trello1.serializers.profile
from trello1.custom.custommodelviewset import *
from trello1.custom.pagination import CustomPagination
from trello1.models import *


# from trello1.serializers.profile import ProfileSerializer


class ProfileViewset(CustomdeleteModelViewset):
    queryset = Profile.objects.all()
    serializer_class = trello1.serializers.profile.ProfileSerializer
    pagination_class = CustomPagination


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