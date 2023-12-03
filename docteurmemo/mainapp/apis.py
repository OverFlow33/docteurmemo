from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import timedelta
from database_objects.serializers import *
from rest_framework import generics
from datetime import date
from  .permissions import *
import requests

class UserCreateAPIView(generics.CreateAPIView):
    permission_classes  = [AllowAny,]
    serializer_class    = UserSerializer

    def post(self, request, *args, **kwargs):
        user_type = request.data['user_type']
        
        if user_type  == 'caregiver':
            serializer = CaregiverSerializer(data=request.data)
        elif user_type  == 'healthcare_professional':
            serializer = DoctorSerializer(data=request.data)
        elif user_type  == 'patient':
            serializer = PatientSerializer(data=request.data)
        else:
            return Response({'error': 'Invalid user type'}, status=status.HTTP_400_BAD_REQUEST)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DoctorCreateAPIView(generics.CreateAPIView):
    permission_classes  = [AllowAny,]
    serializer_class    = DoctorSerializer

class CaregiverCreateAPIView(generics.CreateAPIView):
    permission_classes  = [AllowAny,]
    serializer_class    = CaregiverSerializer

class PatientCreateAPIView(generics.CreateAPIView):
    permission_classes  = [AllowAny,]
    serializer_class    = PatientSerializer


class CountPatientByMemoryScore(APIView):
    permission_classes  = [AllowAny,]
    
    def get(self, request, *args, **kwargs):
        memory_score    = request.query_params.get('memory_score')
        min_age         = request.query_params.get('min_age')
        max_age         = request.query_params.get('max_age')
        patients        = Patient.objects

        if memory_score:
            patients = patients.filter(memory_score__gt=memory_score)
        if min_age:
            min_date = date.today() - timedelta(days=int(min_age) * 365.25)
            patients = patients.filter(birthday__lt=min_date)
        if max_age:
            max_date = date.today() - timedelta(days=int(max_age) * 365.25)
            patients = patients.filter(birthday__gt=max_date)

        patients = patients.count()

        return Response(patients, status=status.HTTP_200_OK)

class PredictPatientScoreAPIView(APIView):
    permission_classes  = [IsAuthenticated, CanPredict]

    def get(self, request, *args, **kwargs):
        name        = request.query_params.get('name')
        r = requests.get('http://localhost:8001/api/v1/predict/', params={'name': name})

        if r.status_code == 200:
            return Response(r.content, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)