from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from database_objects.serializers import *
from database_objects.models import *
        
class PredictPatient(generics.RetrieveAPIView):
    serializer_class    = PatientSerializer
    permission_classes  = [AllowAny,]

    def get_queryset(self, name):
        return Patient.objects.filter(name=name).first()

    def get(self, request, *args, **kwargs):
        name        = request.query_params.get('name')
        patient    = self.get_queryset(name)

        if patient:
            if patient.age > 50:
                score = patient.memory_score + 5
            else:
                score = patient.memory_score + 3

            return Response(score, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)