from django.urls import path
from . import views
from .apis import *

urlpatterns = [
    path('api/v1/predict/', PredictPatient.as_view(), name='predict'),
]