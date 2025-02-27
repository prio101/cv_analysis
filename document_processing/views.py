"""View for handling document uploads."""
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Document
from django.core.exceptions import ObjectDoesNotExist
from .serializers import DocumentSerializer
from .tasks import process_ocr

class DocumentResourcesView(APIView):
    """Document view for handling document uploads.
       INDEX and CREATE
    """

    parser_classes = (MultiPartParser, FormParser)

    def get(self, request):
        """GET METHOD for get all documents."""
        documents = Document.objects.all()
        serializer = DocumentSerializer(documents, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        """POST METHOD for create a new document with uploaded file."""
        file_serializer = DocumentSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            # Enqueuing the task to process the `OCR` via Celery and Redis
            process_ocr.delay(file_serializer.data['id'])

            return Response(file_serializer.data, status=status.HTTP_201_CREATED)

        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DocumentView(APIView):
    """Document view for handling document uploads.
      For specific Documents
    """
    def put(self, request, pk):
        """PUT METHOD for update the status of the document."""
        breakpoint()
        document = Document.objects.get(pk=pk)
        serializer = DocumentSerializer(document, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        """GET METHOD for get a document by id."""
        try:
            document = Document.objects.get(pk=pk)
            serializer = DocumentSerializer(document)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        """DELETE METHOD for delete a document."""
        document = Document.objects.get(pk=pk)
        document.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
