from django.shortcuts import render
# from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets

from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.viewsets import ModelViewSet


class OrganizationViewset(viewsets.ModelViewSet):
    queryset= Organization.objects.all()
    serializer_class = OrganizationSerializer

class BoardViewset(viewsets.ModelViewSet):
    queryset= Board.objects.all()
    serializer_class = BoardSerializer