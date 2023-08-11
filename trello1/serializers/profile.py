
from trello1.models import *
from rest_framework import serializers




class ProfileSerializer(serializers.ModelSerializer):
    # organization = OrganizationSerializer()
    # board = CustomBoardSerializer(many=True)
    board = serializers.ListField(child=serializers.IntegerField(), write_only=True)

    class Meta:
        model = Profile
        fields = "__all__"

    def to_representation(self, instance):
        data = super(ProfileSerializer, self).to_representation(instance)
        return data

    def create(self, validated_data):
        """
        we want to made create method like user can add multiple board
        """
        board_list = validated_data.pop('board')
        organization = validated_data.get('organization')
        boards = organization.boards.all()
        if len(boards) != 0:
            c = 0
            for b in board_list:
                for i in boards:
                    if b == i.id:
                        c += 1
            if c == 0:
                raise serializers.ValidationError(detail="wrong board select")
        instance = Profile.objects.create(**validated_data)
        list_of_boards = organization.boards.filter(id__in=board_list)
        instance.board.set(list_of_boards)
        return instance

    def update(self, instance, validated_data):
        """
              we want to made update method like user can add multiple board
         """

        board_list = validated_data.pop('board')
        organization = validated_data.get('organization')
        boards = organization.boards.all()
        if len(boards) != 0:
            c = 0
            for b in board_list:
                for i in boards:
                    if b == i.id:
                        c += 1
            if c == 0:
                raise serializers.ValidationError(detail="wrong board select")
        list_of_boards = organization.boards.filter(id__in=board_list)
        instance.board.set(list_of_boards)
        return instance