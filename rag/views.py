from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .tasks import process_added_data_for_embedding

class RagView(APIView):
    """API endpoint for querying the RAG model."""

    def get(self, request):
        """GET METHOD for get all documents. To start the processing of the documents texts for embedding."""
        process_added_data_for_embedding.delay()
        message = "Welcome to the RAG API! The Delayed Job has been added to process the documents extracted data"
        return Response({"response": message }, status=status.HTTP_200_OK)
