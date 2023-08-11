import trello1
from trello1.models import *
from rest_framework import serializers


class BoardSerializer(serializers.ModelSerializer):
    organization = trello1.serializers.organization.OrganizationSerializer(read_only=True)

    class Meta:
        model = Board
        fields = "__all__"

    def to_representation(self, instance):
        data = super(BoardSerializer, self).to_representation(instance)
        data.pop('location', None)
        return data


class CustomBoardSerializer(BoardSerializer):
    class Meta:
        model = Board
        fields = "__all__"
        # extra_kwargs = {'name': {'read_only': True},
        #                 'description': {'read_only': True},
        #                 'id': {'required': True}, }

    def to_representation(self, instance):
        data = super(CustomBoardSerializer, self).to_representation(instance)
        data.pop('organization', None)
        return data
