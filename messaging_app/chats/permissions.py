from rest_framework import permissions

class IsParticipant(permissions.BasePermission):
    """
    Only allow access if the user is a participant of the conversation.
    """
    def has_object_permission(self, request, view, obj):
        return request.user in obj.participants.all()


class IsMessageSenderOrParticipant(permissions.BasePermission):
    """
    Only allow the sender or participants of the conversation to access a message.
    """
    def has_object_permission(self, request, view, obj):
        return request.user == obj.sender or request.user in obj.conversation.participants.all()
