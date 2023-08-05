from rest_framework import viewsets
from rest_framework.request import Request
from trello1.models import *
from rest_framework.exceptions import NotFound


class CustomLocationModelViewset(viewsets.ModelViewSet):
    def get_queryset(self):
        if self.action == 'list':
            user = self.request.user
            try:
                member_object = Profile.objects.get(id=user.id)
            except NotFound:
                raise "user is not valid"
            organization = member_object.organization
            queryset = organization.locations.all()
            return queryset
        if self.action == 'retrieve':
            user = self.request.user
            pk = self.kwargs['address1']
            try:
                member_object = Profile.objects.get(id=user.id)
            except NotFound:
                raise "user is not valid"
            try:
                organization = member_object.organization
                self.queryset = organization.locations.get(address1=pk)
            except:
                self.queryset = None
            return self.queryset
        return super().get_queryset()


class CustomBoardModelViewset(viewsets.ModelViewSet):
    def get_queryset(self):
        if self.action == 'list':
            user = self.request.user
            try:
                member_object = Profile.objects.get(user_id=user.id)
            except NotFound:
                raise "user is not valid"
            queryset = member_object.board.all()
            return queryset

        if self.action == 'retrieve':
            user = self.request.user
            pk = self.kwargs['pk']
            try:
                member_object = Profile.objects.get(user_id=user.id)
            except NotFound:
                raise "user is not valid"
            try:
                queryset = member_object.board.get(id=pk)
            except:
                queryset = None
            return queryset
        return super().get_queryset()


class CustomCardModelViewset(viewsets.ModelViewSet):
    def get_queryset(self):
        if self.action == 'list':
            user = self.request.user
            board = self.kwargs['board']
            board_obj = Board.objects.get(name=board)
            queryset = board_obj.cards_on_board.all()
            return queryset
