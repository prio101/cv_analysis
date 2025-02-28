from django.test import TestCase
from chatapp.models import ChatSession, ChatMessage

class ChatSessionTest(TestCase):
    def test_create_chat_session(self):
        session = ChatSession.objects.create()
        self.assertIsNotNone(session.id)
        self.assertIsNotNone(session.created_at)
        self.assertIsNotNone(session.last_active_at)
        self.assertEqual(str(session), f"Session {session.id}")

class ChatMessageTest(TestCase):
    def setUp(self):
        self.session = ChatSession.objects.create()

    def test_create_chat_message(self):
        message = ChatMessage.objects.create(session=self.session, content="Hello, world!")
        self.assertEqual(message.session, self.session)
        self.assertEqual(message.content, "Hello, world!")
        self.assertIsNotNone(message.created_at)
        self.assertEqual(str(message), f"Message {message.id} in {self.session}")
