import openai
from .utils import collection

OPENAI_API_KEY = "your_openai_api_key"

def get_embedding(text):
    response = openai.Embedding.create(
        input=text,
        model="text-embedding-ada-002",
        api_key=OPENAI_API_KEY
    )
    return response["data"][0]["embedding"]

def add_document(id, text, metadata={}):
    embedding = get_embedding(text)
    collection.add(
        ids=[id],
        embeddings=[embedding],
        documents=[text],
        metadatas=[metadata]
    )
