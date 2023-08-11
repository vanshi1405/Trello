from django.shortcuts import render
# from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, permissions

from trello1.custom.custommodelviewset import *

from trello1.custom.pagination import CustomPagination
from rest_framework import status
from trello1.models import *
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, IsAuthenticatedOrReadOnly
from rest_framework.request import Request
from trello1.custom import custompermissions
from trello1.serializers.profile import ProfileSerializer


class ProfileViewset(CustomdeleteModelViewset):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
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