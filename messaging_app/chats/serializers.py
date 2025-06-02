from rest_framework import serializers
from .models import user, Conversation, Message


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model
    """
    id = serializers.UUIDField(source='user_id', read_only=True, format='hex')
    created = serializers.DateTimeField(read_only=True)

    class Meta:
        model = user
        fields = ['id', 'email', 'first_name', 'last_name', 'phone_number', 'is_active', 'created']
        read_only_field = ['is_active']


class MessageSerializer(serializers.ModelSerializer):
    """
    Serializer for Message model
    """
    sender = UserSerializer(read_only=True)
    id = serializers.UUIDField(source='message_id', read_only=True, format='hex')

    class Meta:
        model = Message
        fields = ['id', 'sender', 'message_body', 'sent_at']


class ConversationSerializer(serializers.ModelSerializer):
    """
    Serializer for Conversation model
    """
    participants = UserSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)
    id = serializers.UUIDField(source='conversation_id', read_only=True, format='hex')

    class Meta:
        model = Conversation
        fields = ['id', 'participants', 'created_at', 'messages']
