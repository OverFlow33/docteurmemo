from django.test import TestCase
from django.contrib.auth.models import User
from datetime import date
from .models import Caregiver, Patient, Doctor

class ModelTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_caregiver_model(self):
        caregiver = Caregiver.objects.create(name='Test Caregiver', user=self.user)
        self.assertEqual(str(caregiver), 'Test Caregiver')
        self.assertEqual(caregiver.user, self.user)

    def test_patient_model(self):
        birthday = date.today()
        patient = Patient.objects.create(name='Test Patient', birthday=birthday, memory_score=25, caregiver=None, user=self.user)
        self.assertEqual(str(patient), 'Test Patient')
        self.assertEqual(patient.age, date.today().year - birthday.year)
        self.assertEqual(patient.user, self.user)

    def test_doctor_model(self):
        doctor = Doctor.objects.create(name='Test Doctor', field='GNR', user=self.user)
        self.assertEqual(str(doctor), 'Test Doctor')
        self.assertEqual(doctor.user, self.user)

    def test_patient_with_caregiver(self):
        caregiver = Caregiver.objects.create(name='Test Caregiver', user=self.user)
        patient = Patient.objects.create(name='Test Patient', birthday=date.today(), memory_score=30, caregiver=caregiver, user=self.user)
        self.assertEqual(patient.caregiver, caregiver)
        self.assertIn(patient, caregiver.patients.all())

    def test_patient_age_calculation(self):
        birthday = date.today().replace(year=date.today().year - 25)  # Simulate a patient born 25 years ago
        patient = Patient.objects.create(name='Test Patient', birthday=birthday, memory_score=35, caregiver=None, user=self.user)
        self.assertEqual(patient.age, 25)

    def test_doctor_field_choices(self):
        doctor = Doctor.objects.create(name='Test Doctor', field='PSY', user=self.user)
        self.assertIn(doctor.field, dict(Doctor._meta.get_field('field').choices).keys())
