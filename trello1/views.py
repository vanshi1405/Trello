from django.shortcuts import render
# from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, permissions

from .custom.custommodelviewset import *
from .custom.pagination import CustomPagination
from rest_framework import status
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, IsAuthenticatedOrReadOnly
from rest_framework.request import Request


class LocationViewset(CustomLocationModelViewset):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    lookup_field = 'address1'
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            # Check if the user is a superuser, if yes, grant edit permissions
            if self.request.user.is_superuser:
                return [permissions.IsAuthenticated()]
            else:
                return [permissions.IsAuthenticated(), permissions.ReadOnly()]

        # For other actions like 'list' and 'retrieve', allow read permissions
        return [permissions.IsAuthenticated()]


class OrganizationViewset(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    pagination_class = CustomPagination
    basename = 'organization'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.locations.exists():
            instance.delete()
            return Response(data="instance deleted")
        else:
            raise ValidationError("organization does not have location")


class BoardViewset(CustomBoardModelViewset):
    queryset = Board.objects.all()
    serializer_class = CustomBoardSerializer
    pagination_class = CustomPagination

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.cards_on_board.exists():
            raise ValidationError("Board can not delete some cards are on the board")
        else:
            instance.delete()
            return Response(data="instance deleted")


class CardViewset(CustomCardModelViewset):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    pagination_class = CustomPagination


class ProfileViewset(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    pagination_class = CustomPagination

    # def list(self, request, *args, **kwargs):
    #     return Response(data="method not allowed")

    def destroy(self, request, *args, **kwargs):
        return Response(data="method not allowed")

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