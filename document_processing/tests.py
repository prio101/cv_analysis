from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import serializers
from .models import Document
from .serializers import DocumentSerializer

class DocumentSerializerTest(APITestCase):
    def setUp(self):
        self.document_attributes = {
          'file': 'test_file.pdf',
          'created_at': '2023-10-01T00:00:00Z',
          'email': 'test@example.com',
          'status': 'pending',
          'extracted_text': 'Sample extracted text',
          'rag_status': 'not_started'
        }

        self.document = Document.objects.create(**self.document_attributes)
        self.serializer = DocumentSerializer(instance=self.document)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'file', 'created_at', 'email', 'status', 'extracted_text', 'rag_status']))

    def test_email_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['email'], self.document_attributes['email'])

    def test_status_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['status'], self.document_attributes['status'])

    def test_extracted_text_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['extracted_text'], self.document_attributes['extracted_text'])

    def test_rag_status_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['rag_status'], self.document_attributes['rag_status'])
