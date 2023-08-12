from django.shortcuts import render
# from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, permissions
from Trello.settings import *
import trello1.serializers.organization
from trello1.custom.custommodelviewset import *

from trello1.custom.pagination import CustomPagination
from rest_framework import status
# from trello1.serializers.organization import OrganizationSerializer
from trello1.models import *
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, IsAuthenticatedOrReadOnly
from rest_framework.request import Request
from trello1.task import *
from trello1.custom import custompermissions


class OrganizationViewset(CustomOrganizationViewset):
    queryset = Organization.objects.all()
    serializer_class = trello1.serializers.organization.OrganizationSerializer
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

    @action(detail=False, methods=['GET'])
    def email_send_for_pending_task(self,request):
        subject = "Hello"
        message = "This is an async email sent using Celery."
        from_email = EMAIL_HOST_USER
        recipient_list = ["niteshshah475@gmail.com"]
        send_email.delay()
        return Response(data="mail will be send within min")