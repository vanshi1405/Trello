from .models import *
from rest_framework import serializers


class ChecklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checklist
        fields = "__all__"


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class OrganizationSerializer(serializers.ModelSerializer):
    locations = LocationSerializer(many=True)

    class Meta:
        model = Organization
        fields = "__all__"

    def validate(self, attrs):
        if 'locations' not in attrs:
            raise serializers.ValidationError("Company must have 'locations' attribute")

        location = attrs.get('locations')
        if len(location) == 0:
            raise serializers.ValidationError(detail="company should atleast one location")
        return attrs

    def create(self, validated_data):
        locations = validated_data.pop("locations")
        org = Organization.objects.create(**validated_data)

        location_list = []
        for i in locations:
            location_list.append(Location(organization=org,
                                          country=i.get("country"),
                                          state=i.get("state"),
                                          city=i.get("city"),
                                          address1=i.get("address1")
                                          ))
        Location.objects.bulk_create(location_list)
        org.save()
        return org


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


class CardSerializer(serializers.ModelSerializer):
    checklists = ChecklistSerializer(many=True)

    class Meta:
        model = Card
        fields = "__all__"
