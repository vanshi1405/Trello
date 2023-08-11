from django.shortcuts import render
# from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, permissions

import trello1
from trello1.custom.custommodelviewset import *
from trello1.custom.pagination import CustomPagination
from rest_framework import status
from trello1.models import *
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, IsAuthenticatedOrReadOnly
from rest_framework.request import Request
from trello1.custom import custompermissions
from trello1.serializers import card


class CardViewset(CustomCardModelViewset):
    queryset = Card.objects.all()
    serializer_class =card.CardSerializer
    pagination_class = CustomPagination
