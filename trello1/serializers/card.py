import trello1
from trello1.models import *
from rest_framework import serializers




class CardSerializer(serializers.ModelSerializer):
    checklist = trello1.serializers.checklist.ChecklistSerializer(many=True,required=False)

    class Meta:
        model = Card
        fields = "__all__"

    def create(self, validated_data):
        checklists = validated_data.pop("checklist")
        instance = Card.objects.create(**validated_data)
        check_list = []
        for checklist in checklists:
            check_list.append(Checklist(card=instance,
                                        name=checklist.get("name"),
                                        is_checked=checklist.get("is_checked",False)))
        Checklist.objects.bulk_create(objs=check_list)
        return instance

    def update(self, instance, validated_data):
        pass