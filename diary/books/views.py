from rest_framework import viewsets, permissions, mixins

from .models import Book, Note
from .serializers import BookSerializer, NoteSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
