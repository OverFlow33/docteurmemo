from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework.test import APITestCase

class MyAPITestCase(APITestCase):
    def test_create_caregiver(self):
        data = {
            'user': {
                'username': 'testuser',
                'password': 'testpassword',
            },  
            'user_type': 'caregiver',
            'name': 'caregiver',
        }

        response = self.client.post('/api/v1/users/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('id', response.data)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')

    def test_create_healthcare_professional(self):
        data = {
            'user': {
                'username': 'testuser',
                'password': 'testpassword',
            },            
            'user_type': 'healthcare_professional',
            'field': 'PSY',
        }

        response = self.client.post('/api/v1/users/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('id', response.data)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')

    def test_create_patient(self):
        data = {
            'user': {
                'username': 'testuser',
                'password': 'testpassword',
            },            
            'user_type': 'patient',
            'memory_score': 50,
            'birthday': '1990-01-01',
        }

        response = self.client.post('/api/v1/users/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('id', response.data)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')

    def test_create_invalid_user_type(self):
        data = {
            'username': 'testuser',
            'password': 'testpassword',
            'user_type': 'invalid_type',
        }

        response = self.client.post('/api/v1/users/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)
        self.assertEqual(User.objects.count(), 0)
