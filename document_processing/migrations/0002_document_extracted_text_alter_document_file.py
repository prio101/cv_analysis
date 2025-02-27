# Generated by Django 4.2.19 on 2025-02-27 18:31

from django.db import migrations, models
import document_processing.validators.file_validator


class Migration(migrations.Migration):

    dependencies = [
        ('document_processing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='extracted_text',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(upload_to='documents/', validators=[document_processing.validators.file_validator.validate_file_extension, document_processing.validators.file_validator.validate_file_size]),
        ),
    ]
