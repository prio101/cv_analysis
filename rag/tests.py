from django.test import TestCase
from unittest.mock import patch, MagicMock
from document_processing.models import Document, DocumentRagStatus
from rag.tasks import process_added_data_for_embedding, get_embedding, add_document

class ProcessAddedDataForEmbeddingTest(TestCase):
    def setUp(self):
        self.document = Document.objects.create(
            file='test_file.pdf',
            created_at='2023-10-01T00:00:00Z',
            email='test@example.com',
            status='pending',
            extracted_text='Sample extracted text',
            rag_status='pending'
        )

    @patch('rag.tasks.add_document')
    def test_process_added_data_for_embedding_success(self, mock_add_document):
        mock_add_document.return_value = None
        process_added_data_for_embedding()
        self.document.refresh_from_db()
        self.assertEqual(self.document.rag_status, DocumentRagStatus.COMPLETED.value)


class GetEmbeddingTest(TestCase):
    @patch('openai.Embedding.create')
    def test_get_embedding(self, mock_create):
        mock_create.return_value = {"data": [{"embedding": [0.1, 0.2, 0.3]}]}
        embedding = get_embedding("Sample text")
        self.assertEqual(embedding, [0.1, 0.2, 0.3])

class AddDocumentTest(TestCase):
    @patch('rag.tasks.get_embedding')
    @patch('rag.tasks.collection.add')
    def test_add_document(self, mock_collection_add, mock_get_embedding):
        mock_get_embedding.return_value = [0.1, 0.2, 0.3]
        add_document("1", "Sample text", {"title": "Sample title"})
        mock_collection_add.assert_called_once_with(
            ids=["1"],
            embeddings=[[0.1, 0.2, 0.3]],
            documents=["Sample text"],
            metadatas=[{"title": "Sample title"}]
        )
