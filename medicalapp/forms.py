# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 17:54:08 2020

@author: Sonu
"""

from django import forms
from medicalapp.models import PatientInfo

class PatientInfoForm(forms.ModelForm):
    class Meta:
        model=PatientInfo
        fields="__all__"
    