from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Message
from .serializers import MessageSerializer
from django.shortcuts import get_object_or_404


User = get_user_model()

@require_http_methods(["DELETE"])
@login_required
def delete_user(request):
    user = request.user
    username = user.username
    user.delete()
    return JsonResponse({"message": f"User '{username}' and related data deleted."})

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.filter().select_related(
        'sender', 'receiver', 'edited_by', 'parent_message'
    ).prefetch_related('replies')
    serializer_class = MessageSerializer

    @action(detail=True, methods=['get'], url_path='thread')
    def get_thread(self, request, pk=None):
        """
        Custom action to return all threaded replies to a message
        """
        message = get_object_or_404(Message, pk=pk)
        thread_replies = message.get_thread()
        serializer = self.get_serializer(thread_replies, many=True)
        return Response(serializer.data)
