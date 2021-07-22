from rest_framework import serializers
from Participants.models import Participants


class ParticipantsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participants
        fields = ('id')


class ParticipantsDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Participants
        fields = '__all__'
