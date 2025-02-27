"""Models for the related to document processing Application."""
from django.db import models
from .validators.file_validator import validate_file_extension, validate_file_size

# model for the document submitted by applicant
class Document(models.Model):
    """
      Model for the document submitted
    """
    # document title
    title = models.CharField(max_length=255, blank=False)
    # document file
    file = models.FileField(upload_to='documents/', validators= [validate_file_extension, validate_file_size])
    # email of the applicant
    email = models.EmailField(blank=False)
    # status of the document
    status = models.CharField(max_length=255, default='pending')
    # date of submission
    created_at = models.DateTimeField(auto_now_add=True)

    # default manager
    objects = models.Manager()

    def __str__(self):
        return str(self.title)

    class Meta:
        """Meta definition order for Document."""
        ordering = ['created_at']
