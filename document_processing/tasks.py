from celery import shared_task
from document_processing.models import Document, DocumentStatus
from document_processing.services.process_uploaded_file_service import ProcessUploadedFileService

@shared_task
def process_ocr(document_id):
    """
    Task to process the OCR of the document.
    """
    document = Document.objects.get(id=document_id)
    # call the service to process the OCR
    process_uploaded_file_service = ProcessUploadedFileService()
    if document.file.url:
        process_uploaded_file_service.run(document.file.url)
        # update the document with the extracted text
        document.extracted_text = process_uploaded_file_service.extracted_text
        document.status = DocumentStatus.APPROVED.value
        document.save()

    return document.id
