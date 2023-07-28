from .models import *
from rest_framework import serializers


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['country']


class OrganizationSerializer(serializers.ModelSerializer):
    locations = LocationSerializer(many=True)

    class Meta:
        model = Organization
        fields = "__all__"

class BoardSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer(read_only=True)

    class Meta:
        model = Board
        fields = "__all__"

    def to_representation(self, instance):
        # Get the original representation of the Board model
        data = super(BoardSerializer, self).to_representation(instance)
        # Remove the 'location' field from the representation
        data.pop('location', None)
        return data