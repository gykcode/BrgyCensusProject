from django import forms
from .models import CensusFormModel

class CensusForm(forms.ModelForm):
    # enumeration_area_number = forms.CharField(max_length=200)
    # building_serial = forms.CharField(max_length=200)
    # housing_unit_serial_number = forms.CharField(max_length=200)
    # line_number_respondents = forms.CharField(max_length=200)
    # last_name = forms.CharField(max_length=200)
    # first_name = forms.CharField(max_length=200)
    # address = forms.CharField(max_length=200)
    class Meta:
        model = CensusFormModel
        fields = '__all__'  # Or specify the specific fields you want to include

