from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from database_objects.models import *

class PredictPatientAPITest(APITestCase):
    def setUp(self):
        self.user   = User.objects.create_user(username='testuser', password='testpassword')
        self.patient = Patient.objects.create(name='TestPatient', birthday='1970-01-01', memory_score=20, user=self.user)

    def test_predict_patient_above_50(self):
        response = self.client.get('/api/v1/predict/', {'name': 'TestPatient'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, 25)  # Memory score + 5

    def test_predict_patient_below_50(self):
        # Change the patient's age to below 50
        self.patient.birthday = '1990-01-01'
        self.patient.save()

        response = self.client.get('/api/v1/predict/', {'name': 'TestPatient'})
        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, 23)  # Memory score + 3

    def test_predict_patient_not_found(self):
        response = self.client.get('/api/v1/predict/', {'name': 'NonExistentPatient'})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

