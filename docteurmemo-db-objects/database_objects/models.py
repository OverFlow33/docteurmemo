from django.db import models
from django.contrib.auth.models import User
from datetime import date

FIELDS = (
    ('GNR', 'General Practitioner'),
    ('PSY', 'Psychologist'),
    ('NRL', 'Neurologist'),
)

class Caregiver(models.Model):
    name    = models.CharField(verbose_name='Name', max_length=100)
    user    = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Patient(models.Model):
    name            = models.CharField(verbose_name='Name', max_length=100)
    birthday        = models.DateField(verbose_name='Birthday')
    memory_score    = models.PositiveIntegerField(verbose_name='Memory Score')
    caregiver       = models.ForeignKey(Caregiver, on_delete=models.SET_NULL, related_name="patients", null=True)
    user            = models.OneToOneField(User, on_delete=models.CASCADE)
 
    def __str__(self):
        return self.name
    
    @property
    def age(self):
        return date.today().year - self.birthday.year
    
class Doctor(models.Model):
    name    = models.CharField(verbose_name='Name', max_length=100)
    field   = models.CharField(verbose_name='Status', max_length=3, choices=FIELDS, default='GNR')
    user    = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
