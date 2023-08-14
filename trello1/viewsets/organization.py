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
        user = request.user
        subject = "Trello card Reminder"
        message = f"This is an  email sent from {user.username} ❤, to let you know your card is still in ToDo or doing ."
        from_email = EMAIL_HOST_USER
        recipient_list = []

        profile = Profile.objects.prefetch_related("organization").get(user_id=user.id)
        org = profile.organization
        boards = org.boards.prefetch_related("cards_on_board__user__user")
        for board in boards:
            cards = board.cards_on_board.filter(status__in=["ToDo","Doing"])
            for card in cards:
                user = card.user.user
                recipient_list.append(user.email if user.email not in recipient_list else "")
        send_email.delay(subject,message,from_email,recipient_list)
        return Response(data="mail will be send within minute for all pending card ")