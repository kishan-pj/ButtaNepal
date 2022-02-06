from django import forms
from . models import *

class CustomerForms(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ("__all__")
