from django.urls import path
from .views import start_chat_session, chat_completion

urlpatterns = [
    path('start-session/', start_chat_session, name='start_chat_session'),
    path('message/', chat_completion, name='chat_completion'),
]
