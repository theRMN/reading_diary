from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status


class UserTests(APITestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='user', password='password')
        self.manager = get_user_model().objects.create_user(username='manager', password='password', role='manager')
        self.admin = get_user_model().objects.create_user(username='admin', password='password', role='admin')

    def test_create_user(self):
        url = reverse('UserViewSet-list')
        data = {'username': 'new_user', 'password': 'password'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_change_user_by_manager(self):
        user = get_user_model().objects.create_user(username='testuser', password='password')
        self.client.force_authenticate(user=self.manager)

        url = reverse('UserViewSet-detail', args=[user.id])
        data = {'role': 'manager'}
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_change_user_by_admin(self):
        user = get_user_model().objects.create_user(username='testuser', password='password')
        self.client.force_authenticate(user=self.admin)

        url = reverse('UserViewSet-detail', args=[user.id])
        data = {'role': 'manager'}
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

