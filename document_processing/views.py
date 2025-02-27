from django.shortcuts import render
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Document
from .serializers import DocumentSerializer


class DocumentView(APIView):
    """Document view for handling document uploads."""
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        """POST METHOD for create a new document with uploaded file."""
        file_serializer = DocumentSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)

        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, _):
        """GET METHOD for get all documents."""
        documents = Document.objects.all()
        serializer = DocumentSerializer(documents, many=True)
        return Response(serializer.data)
