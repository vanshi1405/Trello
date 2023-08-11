from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from trello1.models import *
from rest_framework.exceptions import NotFound


class CustomOrganizationViewset(viewsets.ModelViewSet):
    def get_queryset(self):
        user = self.request.user
        if self.action == 'list':
            try:
                member_object = Profile.objects.get(user_id=user.id)
            except NotFound:
                raise "user is not valid"
            if member_object.user_type == "organization_admin":
                queryset = Organization.objects.all()
                return queryset
            else:
                queryset = member_object.organization
                return [queryset]

        if self.action == 'retrive':
            pk = self.kwargs['pk']
            try:
                member_object = Profile.objects.get(user_id=user.id)
            except NotFound:
                raise "user is not valid"
            if member_object.user_type == "organization_admin":
                queryset = Profile.objects.get(id=int(pk))
                return queryset
        return super().get_queryset()


class CustomLocationModelViewset(viewsets.ModelViewSet):
    def get_queryset(self):
        user = self.request.user
        if self.action == 'list':
            try:
                member_object = Profile.objects.get(user_id=user.id)
            except NotFound:
                raise "user is not valid"
            organization = member_object.organization
            queryset = organization.locations.all()
            return queryset
        if self.action == 'retrieve':
            pk = self.kwargs['pk']
            try:
                member_object = Profile.objects.get(user_id=user.id)
            except NotFound:
                raise "user is not valid"
            try:
                organization = member_object.organization
                self.queryset = organization.locations.get(id=int(pk))
            except:
                self.queryset = None
            return self.queryset
        return super().get_queryset()


class CustomBoardModelViewset(viewsets.ModelViewSet):
    def get_queryset(self):
        user = self.request.user
        if self.action == 'list':
            try:
                member_object = Profile.objects.get(user_id=user.id)
            except NotFound:
                raise "user is not valid"
            queryset = member_object.board.all()
            return queryset

        if self.action == 'retrieve':
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
            board = self.request.query_params.get('board', None)
            board_obj = Board.objects.get(id=int(board))
            queryset = board_obj.cards_on_board.all()
            return queryset
        if self.action == 'retrieve':
            pk = self.kwargs['pk']
            board = self.request.query_params.get('board', None)
            board_obj = Board.objects.get(id=int(board))
            queryset = board_obj.cards_on_board.filter(id=pk)
            return queryset
        return super().get_queryset()


class CustomdeleteModelViewset(viewsets.ModelViewSet):

    def destroy(self, request, *args, **kwargs):
        return Response(data="method not allowed")
