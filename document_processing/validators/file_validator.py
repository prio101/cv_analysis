"""Validation functions for file uploads."""
import os
from django.core.exceptions import ValidationError

def validate_file_extension(value):
    """Function to validate the file extension."""
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf', '.doc', '.docx']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')

def validate_file_size(value):
    """Function to validate the file size."""
    filesize = value.size
    # 10MB is the maximum file size that can be uploaded
    if filesize > ( 10 * 1024 * 1024):
        raise ValidationError('The maximum file size that can be uploaded is 10MB.')
