from django.shortcuts import render
# from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets

from .custom.custommodelviewset import *
from .custom.pagination import CustomPagination
from rest_framework import status
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.viewsets import ModelViewSet


class OrganizationViewset(viewsets.ModelViewSet):
    queryset= Organization.objects.all()
    serializer_class = OrganizationSerializer
    pagination_class = CustomPagination

    def destroy(self, request, *args, **kwargs):
        instance=self.get_object()
        if instance.locations.exists():
            instance.delete()
            return Response(data="instance deleted")
        else:
            raise ValidationError("organization does not have location")


class BoardViewset(CustomBoardModelViewset):
    queryset= Board.objects.all()
    serializer_class = BoardSerializer
    pagination_class = CustomPagination


class CardViewset(CustomCardModelViewset):
    queryset= Board.objects.all()
    serializer_class = CardSerializer
    pagination_class = CustomPagination


