import os
from celery import Celery

# Set default Django settings for Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cv_analysis.settings')

app = Celery('cv_analysis.settings')

# Load configuration from Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks in installed Django apps
app.autodiscover_tasks()
