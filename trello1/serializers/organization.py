import trello1
from trello1.models import *
from rest_framework import serializers

from trello1.serializers import location


class OrganizationSerializer(serializers.ModelSerializer):
    locations = location.LocationSerializer(many=True)

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

    def update(self, instance, validated_data):
        locations = validated_data.pop("locations")
        instance.name = validated_data.pop("name")
        instance.email = validated_data.pop("email")
        instance.mobile_number = validated_data.pop("mobile_number")
        instance.company_size_min_value = validated_data.pop("company_size_min_value")
        instance.company_size_max_value = validated_data.pop("company_size_max_value")
        location_list = []
        instance.locations.all().delete()
        for location in locations:
            location_list.append(Location(organization=instance,
                                          country=location.get("country"),
                                          state=location.get("state"),
                                          city=location.get("city"),
                                          address1=location.get("address1")
                                          ))
        Location.objects.bulk_create(location_list)
        instance.save()
        return instance
