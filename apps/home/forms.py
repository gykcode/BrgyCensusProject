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
            'date_time_created_1','date_time_ended_1','result_1', 'result_description_1',
            'date_time_created_2','date_time_ended_2','result_2', 'result_description_2',
            'date_time_created_3','date_time_ended_3','result_3', 'result_description_3',
            'number_of_visit',
            'result_of_final_visit',
            'number_of_household_member',
            'number_male',
            'number_female',
            'enumerator_code',
            'mode_of_data_collection',
            
            'appointment_date_time_1',
            'appointment_date_time_2',
            'appointment_date_time_3',
        ]  # Or specify the specific fields you want to include

        widgets= {
            
            'enumeration_area_number': forms.TextInput(attrs={'class': 'form-control col-3 inputBorder '}),
            'building_serial': forms.TextInput(attrs={'class': 'form-control col-3 inputBorder '}),
            'housing_unit_serial_number': forms.TextInput(attrs={'class': 'form-control col-3 inputBorder '}),
            'household_serial_number': forms.TextInput(attrs={'class': 'form-control col-3 inputBorder '}),
            'line_number_respondents': forms.TextInput(attrs={'class': 'form-control col-3 inputBorder '}),
            'last_name': forms.TextInput(attrs={'class': 'form-control col-3 inputBorder bottomInputMargin '}),
            'first_name': forms.TextInput(attrs={'class': 'form-control col-3 inputBorder bottomInputMargin ml-3 '}),
            'address': forms.TextInput(attrs={'class': 'form-control col-8 inputBorder '}),

            'date_time_created_1' : forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control col-7 inputBorder mt-1 mr-1'}),
            'date_time_ended_1' : forms.TimeInput(attrs={'type': 'datetime-local', 'class': 'form-control col-7 inputBorder mt-1 mr-1'}),
            'result_1' : forms.Select(attrs={'class': 'form-control col-7 inputBorder mt-1 mr-1', 'onchange': 'handleResultChange()'}),
            'result_description_1': forms.TextInput(attrs={'class': 'form-control col-7 inputBorder mt-1 mr-1', 'readonly': 'readonly'}),

            'number_of_visit': forms.TextInput(attrs={'class': 'form-control col-12 inputBorder mt-1 '}),
            'result_of_final_visit': forms.TextInput(attrs={'class': 'form-control col-12 inputBorder mt-1 '}),
            'number_of_household_member': forms.TextInput(attrs={'class': 'form-control col-12 inputBorder mt-1 '}),
            'number_male': forms.TextInput(attrs={'class': 'form-control col-12 inputBorder mt-1 '}),
            'number_female': forms.TextInput(attrs={'class': 'form-control col-12 inputBorder mt-1 '}),
            'enumerator_code': forms.TextInput(attrs={'class': 'form-control col-12 inputBorder mt-1 '}),
            'mode_of_data_collection': forms.Select(attrs={'class': 'form-control col-12 inputBorder mt-1 needVal'}),

            'appointment_date_time_1' : forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control col-7 inputBorder mt-1 mr-1 mb-2'}),
        }
       