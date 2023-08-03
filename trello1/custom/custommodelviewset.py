from rest_framework import viewsets
from rest_framework.request import Request
from trello1.models import *
from rest_framework.exceptions import NotFound


class CustomBoardModelViewset(viewsets.ModelViewSet):
    def get_queryset(self):
        if self.action == 'list':
            user = self.request.user
            try:
                member_object = Profile.objects.get(id=user.id)
            except NotFound:
                raise "user is not valid"
            queryset = member_object.board.all()
            return queryset

        if self.action == 'retrieve':
            user = self.request.user
            pk = self.kwargs['pk']
            try:
                member_object = Profile.objects.get(id=user.id)
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
            board_obj=Board.objects.get(name=board)
            queryset=board_obj.cards_on_board.all()
            return queryset

