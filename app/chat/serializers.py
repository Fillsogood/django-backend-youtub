from rest_framework import serializers
from .models import ChatRoom, CahtMessage
class CahtRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = ('__all__')

class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CahtMessage
        fields = ('__all__')
        read_only_fields = ['room', 'sender']
