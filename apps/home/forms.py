from django import forms
from .models import CensusFormModel

class CensusForm(forms.ModelForm):

    class Meta:
        model = CensusFormModel
        fields = '__all__'  # Or specify the specific fields you want to include

def clean(self):
    clean_data = super().clean()