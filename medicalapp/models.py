from django.db import models
from django.utils import timezone
from medical.settings import DATE_INPUT_FORMATS

# Create your models here.
    
    
class PatientInfo(models.Model):
    Fname=models.CharField(max_length=100)
    Lname=models.CharField(max_length=500)
    Age=models.IntegerField()
    sex=models.CharField(max_length=200)
    Contact=models.CharField(max_length=1000)
    Email=models.EmailField(max_length=100)
    Address=models.TextField()
    city=models.CharField(max_length=400)
    state=models.CharField(max_length=500)
    reason=models.TextField()
    medicine=models.TextField(default='',blank=True)
    report=models.TextField(default='',blank=True)
    patient=models.TextField(default='',blank=True)
    tablet=models.TextField(default='',blank=True)
    
    class Meta:
        db_table='patientinfo'