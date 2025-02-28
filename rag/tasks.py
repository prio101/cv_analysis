import openai
import os
from celery import shared_task
from document_processing.models import Document
from rag.utils import collection

@shared_task
def process_added_data_for_embedding():
    """
    Task to process the added data for embedding.
    """
    for document in Document.objects.filter(extracted_text__isnull=False, rag_status="pending"):
        id_to_str = str(document.id)
        try:
            add_document(id_to_str, document.extracted_text, {"title": document.title})
            # update the document with the rag status
            document.rag_status = "completed"
        except (openai.error.OpenAIError, ValueError, TypeError) as e:
            # update the document with the rag status as failed
            document.rag_status = "failed"
            document.error_message = str(e)
        finally:
            document.save()

def get_embedding(text):
    """Get the embedding for the given text."""
    response = openai.Embedding.create(
      input=text,
      model="text-embedding-ada-002",  # Specify the embedding model
      api_key=os.getenv("OPENAI_API_KEY")
    )
    return response["data"][0]["embedding"]

def add_document(id, text, metadata={}):
    """Add a document to ChromaDB."""
    embedding = get_embedding(text)

    # Ensure metadata is always a list of dictionaries
    if isinstance(metadata, dict):
        metadata = [metadata]  # Wrap metadata in a list if it's a single dictionary
    elif not metadata:
        metadata = [{}]  # Use an empty dictionary if metadata is empty

    collection.add(
        ids=[id],
        embeddings=[embedding],
        documents=[text],
        metadatas=metadata  # Pass metadata as a list of dictionaries
    )
