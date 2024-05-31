from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions

from django_filters.rest_framework import DjangoFilterBackend

from .models import Book, Note
from .filters import SearchBook, SearchNote
from .serializers import BookSerializer, NoteSerializer
from .permissions import IsAuthorOrIsAdmin


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SearchBook
    permission_classes = (permissions.IsAuthenticated, IsAuthorOrIsAdmin,)

    def get_queryset(self):

        if self.request.user.role == get_user_model().USER:
            queryset = Book.objects.filter(user=self.request.user)
        else:
            queryset = Book.objects.all()

        return queryset


class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SearchNote
    permission_classes = (permissions.IsAuthenticated, IsAuthorOrIsAdmin,)

    def get_queryset(self):

        if self.request.user.role == get_user_model().USER:
            queryset = Note.objects.filter(book__user=self.request.user)
        else:
            queryset = Note.objects.all()

        return queryset
