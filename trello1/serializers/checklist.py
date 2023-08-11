import trello1
from trello1.models import *
from rest_framework import serializers


class ChecklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checklist
        fields = "__all__"

    def get_fields(self):
        fields = super().get_fields()
        if isinstance(self.context['view'], trello1.viewsets.card.CardViewset):
            fields['card'].read_only = True
        return fields