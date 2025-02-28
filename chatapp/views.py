import openai
import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from chatapp.middleware import use_token, get_tokens
from .models import ChatSession, ChatMessage
from rag.serializers import RagQuerySerializer
from rag.embeddings import generate_response


@api_view(['POST'])
def start_chat_session(request):
    """Start a new chat session and return the session ID."""
    chat_session = ChatSession.objects.create()
    return Response({"chat_session_id": str(chat_session.id)})

@api_view(['POST'])
def chat_completion(request):
    """Handle chat messages with rate limiting."""
    chat_session_id = request.data.get("chat_session_id")
    user_message = request.data.get("message")

    if not chat_session_id or not user_message:
        return Response({"error": "chat_session_id and message are required."}, status=status.HTTP_400_BAD_REQUEST)

    # Check token bucket
    if not use_token(chat_session_id):
        return Response({"error": "Rate limit exceeded. Try again later."}, status=status.HTTP_429_TOO_MANY_REQUESTS)


    serializer = RagQuerySerializer(data=request.data)

    if serializer.is_valid():
        query = serializer.validated_data["query"]
        response = generate_response(query)
        # before returning save the response in the database
        chat_session = ChatSession.objects.get(id=chat_session_id)
        try:
            ChatMessage.objects.create(
                chat_session=chat_session,
                content=response
            )
        except (ChatMessage.DoesNotExist, ChatSession.DoesNotExist) as e:
            return Response({"error": f"Error saving chat message: {e}"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"response": response}, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
