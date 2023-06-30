from django import forms
from .models import CensusFormModel
import datetime

class CensusForm(forms.ModelForm):
    class Meta:
        model = CensusFormModel
        fields = [
            'enumeration_area_number',
            'building_serial', 
            'housing_unit_serial_number', 
            'household_serial_number', 
            'line_number_respondents', 
            'last_name', 
            'first_name', 
            'address',
            'date_1',
            'time_begin_1',
            'time_ended_1',
            'number_of_visit',
            'result_of_final_visit',
            'number_of_household_member',
            'number_male',
            'number_female',
            'enumerator_code',
            'mode_of_data_collection',
        ]  # Or specify the specific fields you want to include

        widgets= {
            
            'enumeration_area_number': forms.TextInput(attrs={'class': 'form-control col-3 inputBorder needVal'}),
            'building_serial': forms.TextInput(attrs={'class': 'form-control col-3 inputBorder needVal'}),
            'housing_unit_serial_number': forms.TextInput(attrs={'class': 'form-control col-3 inputBorder needVal'}),
            'household_serial_number': forms.TextInput(attrs={'class': 'form-control col-3 inputBorder needVal'}),
            'line_number_respondents': forms.TextInput(attrs={'class': 'form-control col-3 inputBorder needVal'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control col-3 inputBorder bottomInputMargin needVal'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control col-3 inputBorder bottomInputMargin ml-3 needVal'}),
            'address': forms.TextInput(attrs={'class': 'form-control col-8 inputBorder needVal'}),

            'date_1' : forms.DateTimeInput(attrs={'class': 'form-control col-2 inputBorder mt-1 mr-1 datePick ', 'placeholder': 'mm/dd'}),
            'time_begin_1' : forms.DateTimeInput(attrs={'class': 'form-control col-2 inputBorder mt-1 mr-1 datePick ', 'placeholder': 'am/pm'}),
            'time_ended_1' : forms.DateTimeInput(attrs={'class': 'form-control col-2 inputBorder mt-1 mr-1 datePick ', 'placeholder': 'am/pm'}),

            'number_of_visit': forms.TextInput(attrs={'class': 'form-control col-12 inputBorder mt-1 needVal'}),
            'result_of_final_visit': forms.TextInput(attrs={'class': 'form-control col-12 inputBorder mt-1 needVal'}),
            'number_of_household_member': forms.TextInput(attrs={'class': 'form-control col-12 inputBorder mt-1 needVal'}),
            'number_male': forms.TextInput(attrs={'class': 'form-control col-12 inputBorder mt-1 needVal'}),
            'number_female': forms.TextInput(attrs={'class': 'form-control col-12 inputBorder mt-1 needVal'}),
            'enumerator_code': forms.TextInput(attrs={'class': 'form-control col-12 inputBorder mt-1 needVal'}),
            'mode_of_data_collection': forms.TextInput(attrs={'class': 'form-control col-12 inputBorder mt-1 needVal'}),
        }