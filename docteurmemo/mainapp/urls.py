from django.urls import path
from .apis import *
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('api/v1/users/', UserCreateAPIView.as_view(), name='create_user'),

    path('api/v1/doctors/', DoctorCreateAPIView.as_view(), name='create_doctor'),
    path('api/v1/caregivers/', CaregiverCreateAPIView.as_view(), name='create_caregiver'),
    path('api/v1/patients/', PatientCreateAPIView.as_view(), name='create_patient'),
    path('api/v1/patient/count-by-memory-score/', CountPatientByMemoryScore.as_view(), name='count_patients_by_memory_score'),

    path('api/v1/predict-patient-score/', PredictPatientScoreAPIView.as_view(), name='create_user'),

    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]