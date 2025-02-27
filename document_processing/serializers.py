"""Serializers for the document_processing app."""
from rest_framework import serializers
from .models import Document


class DocumentSerializer(serializers.ModelSerializer):
    """Serializer for the Document model."""


    class Meta:
        """Meta class for the DocumentSerializer."""
        model = Document
        fields = ["id", "file", "created_at", "email", "status"]
