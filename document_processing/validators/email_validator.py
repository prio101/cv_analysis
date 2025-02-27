"""Validation functions for email."""
from django.core.exceptions import ValidationError

def validate_email_address(value):
    """Function to validate the email"""
    if "@" not in value or "." not in value or len(value) < 5 or len(value) > 100:
        raise ValidationError("Invalid email address.")
