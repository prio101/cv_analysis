# Generated by Django 4.2.19 on 2025-02-28 10:05

from django.db import migrations, models
import document_processing.validators.email_validator


class Migration(migrations.Migration):

    dependencies = [
        ('document_processing', '0003_document_rag_status_alter_document_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='email',
            field=models.EmailField(blank=True, max_length=254, validators=[document_processing.validators.email_validator.validate_email_address]),
        ),
    ]
