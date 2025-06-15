from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Message, MessageHistory, Notification

@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.receiver,
            message=instance
        )

@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    if instance.id:
        try:
            old_message = Message.objects.get(id=instance.id)
            if old_message.content != instance.content:
                # Save old content to history
                MessageHistory.objects.create(
                    message=instance,
                    old_content=old_message.content
                )
                instance.edited = True
        except Message.DoesNotExist:
            pass  # It's a new message, not an edit