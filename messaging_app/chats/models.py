from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class user(AbstractUser):
    """
    A model description for user
    """
    pass


class conversation(models.Model):
    """
    A model description for conversation
    """
    participants = models.ManyToManyField(user, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation {self.id}"


class message(models.Model):
    """
    A model description for message
    """
    sender = models.ForeignKey(user, on_delete=models.CASCADE, related_name='sent_messages')
    conversation = models.ForeignKey(conversation, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Message {self.id} from {self.sender.username}"
