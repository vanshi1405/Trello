from django.shortcuts import render
# from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, permissions

from trello1.custom.custommodelviewset import *

from trello1.custom.pagination import CustomPagination
from rest_framework import status
from trello1.serializers.organization import OrganizationSerializer
from trello1.models import *
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, IsAuthenticatedOrReadOnly
from rest_framework.request import Request
from trello1.custom import custompermissions




class OrganizationViewset(CustomOrganizationViewset):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    pagination_class = CustomPagination
    basename = 'organization'
    permission_classes = [custompermissions.CustomOrganizationPermissions]


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.locations.exists():
            instance.delete()
            return Response(data="instance deleted")
        else:
            raise ValidationError("organization does not have location")