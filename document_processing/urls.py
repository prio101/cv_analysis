from django.urls import path
from .views import DocumentView, DocumentResourcesView

urlpatterns = [
    path('documents/', DocumentResourcesView.as_view(), name='document_list_view'),
    path('documents/<int:pk>/', DocumentView.as_view(), name='document_view'),
]
