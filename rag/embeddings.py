import os
import openai
from .utils import collection

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def get_embedding(text):
    """Get the text embedding from OpenAI's text-embedding model."""
    response = openai.Embedding.create(
        input=text,
        model="text-embedding-ada-002",
        api_key=OPENAI_API_KEY
    )
    return response["data"][0]["embedding"]

def query_documents(query_text, n_results=3):
    """Retrieve relevant documents from ChromaDB."""
    query_embedding = get_embedding(query_text)
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )
    return results["documents"][0] if results["documents"] else []

def generate_response(query):
    """Generate a response based on retrieved documents."""
    relevant_docs = query_documents(query)
    context = "\n".join(relevant_docs) if relevant_docs else "No relevant documents found."

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI assistant."},
            {"role": "user", "content": f"Context: {context}\n\nQuestion: {query}"}
        ],
        api_key=OPENAI_API_KEY
    )
    return response["choices"][0]["message"]["content"]
