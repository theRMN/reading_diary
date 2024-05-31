from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from .models import Book


class BaseTests(APITestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='user', password='password')
        self.manager = get_user_model().objects.create_user(username='manager', password='password', role='manager')
        self.admin = get_user_model().objects.create_user(username='admin', password='password', role='admin')


class BookTests(BaseTests):

    def test_create_book(self):
        self.client.force_authenticate(user=self.user)

        url = reverse('BookViewSet-list')
        book_data = {'name': 'Sample Book'}
        response = self.client.post(url, book_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_manager_books_view(self):
        self.client.force_authenticate(user=self.manager)

        url = reverse('BookViewSet-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_books_view(self):
        self.client.force_authenticate(user=self.admin)

        url = reverse('BookViewSet-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class NoteTests(BaseTests):

    def test_create_note(self):
        url = reverse('UserViewSet-list')
        data = {'username': 'new_user', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        new_user = get_user_model().objects.get(id=response.data.get('id'))

        self.client.force_authenticate(user=new_user)

        book_data = {'user': new_user, 'name': 'Sample Book'}
        new_book = Book.objects.create(**book_data)
        note_url = reverse('NoteViewSet-list')
        note_data = {'book': new_book.id, 'text': 'Sample text', 'num_pages': 1}
        response = self.client.post(note_url, note_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_manager_note_view(self):
        self.client.force_authenticate(user=self.manager)

        url = reverse('NoteViewSet-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_note_view(self):
        self.client.force_authenticate(user=self.admin)

        url = reverse('NoteViewSet-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
