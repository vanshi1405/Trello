
from trello1.models import *
from rest_framework import serializers


import trello1



class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"
        extra_kwargs = {
            'organization': {'required': True},
        }

    def get_fields(self):
        fields = super().get_fields()
        if isinstance(self.context['view'], trello1.viewsets.organization.OrganizationViewset):
            fields['organization'].read_only = True
        return fields

    def validate(self, attrs):
        if 'organization' not in attrs and isinstance(self.context['view'], trello1.viewsets.location.LocationViewset):
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
