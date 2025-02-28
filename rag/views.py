from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RagQuerySerializer
from .embeddings import get_embedding
from .utils import collection
from .tasks import process_added_data_for_embedding
import openai

OPENAI_API_KEY = "your_openai_api_key"

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

class RagView(APIView):
    """API endpoint for querying the RAG model."""

    def post(self, request):
        serializer = RagQuerySerializer(data=request.data)
        if serializer.is_valid():
            query = serializer.validated_data["query"]
            response = generate_response(query)
            return Response({"response": response}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """GET METHOD for get all documents. To start the processing of the documents texts for embedding."""
        process_added_data_for_embedding.delay()
        return Response({"response": "Welcome to the RAG API! The Delayed Job has been added to process the documents extracted data"}, status=status.HTTP_200_OK)
