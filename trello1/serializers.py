import trello1.views
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
        extra_kwargs = {
            'organization': {'required': True},
        }

    def get_fields(self):
        fields = super().get_fields()
        if isinstance(self.context['view'], trello1.views.OrganizationViewset):
            fields['organization'].read_only = True
        return fields

    def validate(self, attrs):
        if 'organization' not in attrs and isinstance(self.context['view'], trello1.views.LocationViewset):
            raise serializers.ValidationError("location must have 'organization' attribute")
        return attrs

    def create(self, validated_data):
        return Location.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.organization = validated_data.get('organization')
        instance.country = validated_data.pop('country')
        instance.state = validated_data.pop('state')
        instance.city = validated_data.pop('city')
        instance.address1 = validated_data.pop('address1')
        instance.save()
        return instance


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


class BoardSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer(read_only=True)

    class Meta:
        model = Board
        fields = "__all__"

    def to_representation(self, instance):
        data = super(BoardSerializer, self).to_representation(instance)
        data.pop('location', None)
        return data


class CustomBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = "__all__"

    def to_representation(self, instance):
        data = super(CustomBoardSerializer, self).to_representation(instance)
        data.pop('location', None)
        return data


class CardSerializer(serializers.ModelSerializer):
    checklists = ChecklistSerializer(many=True)

    class Meta:
        model = Card
        fields = "__all__"
