from django.apps import AppConfig
import chromadb
from .utils import initialize_chroma

class RagConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rag'

    def ready(self):
        initialize_chroma()
