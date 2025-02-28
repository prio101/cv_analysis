import uuid
from django.db import models
from django.utils.timezone import now

class ChatSession(models.Model):
    """Model to represent a chat session."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_active_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Session {self.id}"

    class Meta:
        """Order by last active time by default."""
        ordering = ["-last_active_at"]

class ChatMessage(models.Model):
    """Model to represent a chat message."""
    session = models.ForeignKey(ChatSession, on_delete=models.CASCADE, related_name="messages")
    content = models.TextField()
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"Message {self.id} in {self.session}"

    class Meta:
        """Order by creation time by default."""
        ordering = ["created_at"]
