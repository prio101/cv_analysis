from django.urls import path
from .views import RagView

urlpatterns = [
    path("run_rag/", RagView.as_view(), name="RagView"),
]
