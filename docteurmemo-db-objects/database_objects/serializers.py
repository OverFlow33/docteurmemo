from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model   = User
        fields  = ['id', 'username', 'password']

        extra_kwargs = {'password': {'write_only': True}}

class CaregiverSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model   = Caregiver
        fields  = '__all__'

    def create(self, validated_data):
        user_data   = validated_data.get('user', [])
        user        = None

        if user_data:
            user = User.objects.create_user(**user_data)

        del validated_data['user']

        instance = Caregiver.objects.create(user=user, **validated_data)       

        return instance

class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model   = Patient
        fields  = '__all__'

    def create(self, validated_data):
        user_data   = validated_data.get('user', [])
        user        = None

        if user_data:
            user = User.objects.create_user(**user_data)

        del validated_data['user']

        instance = Patient.objects.create(user=user, **validated_data)       

        return instance

class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model   = Doctor
        fields  = '__all__'

    def create(self, validated_data):
        user_data   = validated_data.get('user', [])
        user        = None

        if user_data:
            user = User.objects.create_user(**user_data)

        del validated_data['user']

        instance = Doctor.objects.create(user=user, **validated_data)       

        return instance