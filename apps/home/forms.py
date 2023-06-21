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
        fields = (
            'enumeration_area_number',
            'building_serial', 
            'housing_unit_serial_number', 
            'household_serial_number', 
            'line_number_respondents', 
            'last_name', 
            'first_name', 
            'address'
        )  # Or specify the specific fields you want to include

        widgets= {
            'enumeration_area_number': forms.TextInput(attrs={'class': 'form-control col-3 inputBorder'}),
            'building_serial': forms.TextInput(attrs={'class': 'form-control col-3 inputBorder'}),
            'housing_unit_serial_number': forms.TextInput(attrs={'class': 'form-control col-3 inputBorder'}),
            'household_serial_number': forms.TextInput(attrs={'class': 'form-control col-3 inputBorder'}),
            'line_number_respondents': forms.TextInput(attrs={'class': 'form-control col-3 inputBorder'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control col-3 inputBorder bottomInputMargin'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control col-3 inputBorder bottomInputMargin ml-3'}),
            'address': forms.TextInput(attrs={'class': 'form-control col-8 inputBorder'}),
        }

