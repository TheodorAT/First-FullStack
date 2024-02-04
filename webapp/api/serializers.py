from rest_framework import serializers
from .models import Room

# Translating models into JSON format


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        # The model we want to serialize
        model = Room
        fields = ('id', 'code', 'host', 'guest_can_pause',
                  'votes_to_skip', 'created_at')
