"""Utility functions for the RAG project."""
import chromadb
from chromadb.config import Settings
from chromadb import Client
import sqlite3

# Initialize ChromaDB client
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection(name="documents")

# client = Client(Settings(
#     chroma_db_impl="postgresql",  # specify PostgreSQL as backend
#     postgres_url="postgresql://postgres:postgres@localhost/cv_analysis"  # your PostgreSQL connection string
# ))


def initialize_chroma():
    """Initialize ChromaDB client and create a collection."""
    global collection
    if not collection:
        collection = chroma_client.get_or_create_collection(name="documents")



