from django import forms
from .models import CensusFormModel
import datetime

class CensusForm(forms.ModelForm):
    class Meta:
        model = CensusFormModel
        fields = [
            #3A
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
            'appointment_date_time_1','appointment_date_time_2','appointment_date_time_3',

            # 3B
            'residing_fullname_1', 
            'relationship_to_head_1', 
            'gender_1', 
            'date_born_1', 
            'age_1', 
            'birth_registered_1', 
            'copy_birthcert_1', 
            'marital_status_1',
            'not_yet_listed',
            'additional_booklet',

            #3C
            'religion_1', 
            'citizen_1', 
            'other_country_1', 
            'ethnicity_1', 
            'health_problem_a_1', 
            'health_problem_b_1', 
            'health_problem_c_1', 
            'health_problem_d_1', 
            'health_problem_e_1', 
            'health_problem_f_1',
            'remarks_3C',

            #3D
            'province_time_birth_1',
            'municipality_time_birth_1', 
            'province_reside_1', 
            'municipality_reside_1', 
            'read_write_1', 
            'highest_year_completed_1', 
            'attend_school_1', 
            'province_school_attended_1',
            'municipality_school_attended_1',
            'overseas_worker_1', 

            #3E
            'usual_activity_1',
            'business_worked_1',
            'kind_of_worker_1',
            'province_work_past12months_1',
            'municipality_work_past12months_1',
            'children_borned_1',
            'children_still_living_1',
            'children_alive_specificdate_1',
            'age_firstmarriage_1',
            'remarks_3E',
        ]  # Or specify the specific fields you want to include

        widgets= {
            #3A
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
            'result_1' : forms.Select(attrs={'class': 'form-control col-12 inputBorder mt-1 mr-1', 'onchange': 'handleResultChange()'}),
            'result_description_1': forms.TextInput(attrs={'class': 'form-control col-7 inputBorder mt-1 mr-1', 'readonly': 'readonly', 'placeholder': 'Specify Reason'}),

            'number_of_visit': forms.TextInput(attrs={'class': 'form-control col-12 inputBorder mt-1 '}),
            'result_of_final_visit': forms.TextInput(attrs={'class': 'form-control col-12 inputBorder mt-1 '}),
            'number_of_household_member': forms.TextInput(attrs={'class': 'form-control col-12 inputBorder mt-1 '}),
            'number_male': forms.TextInput(attrs={'class': 'form-control col-12 inputBorder mt-1 '}),
            'number_female': forms.TextInput(attrs={'class': 'form-control col-12 inputBorder mt-1 '}),
            'enumerator_code': forms.TextInput(attrs={'class': 'form-control col-12 inputBorder mt-1 '}),
            'mode_of_data_collection': forms.Select(attrs={'class': 'form-control col-12 inputBorder mt-1'}),
            'appointment_date_time_1' : forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control col-7 inputBorder mt-1 mr-1 mb-2'}),
           
            #3B
            'residing_fullname_1': forms.TextInput(attrs={'class': 'form-control col-12 inputBorder '}),
            'relationship_to_head_1': forms.Select(attrs={'class': 'form-control col-12 inputBorder mt-1'}),
            'gender_1': forms.Select(attrs={'class': 'form-control col-12 inputBorder mt-1'}),
            'date_born_1' : forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control col-12 inputBorder mt-1 mr-1 mb-2'}),
            'age_1': forms.TextInput(attrs={'class': 'form-control col-12 inputBorder mt-1 '}),
            'birth_registered_1': forms.Select(attrs={'class': 'form-control col-12 inputBorder mt-1'}),
            'copy_birthcert_1': forms.Select(attrs={'class': 'form-control col-12 inputBorder mt-1'}),
            'marital_status_1': forms.Select(attrs={'class': 'form-control col-12 inputBorder mt-1'}),
            'not_yet_listed': forms.Select(attrs={'class': 'form-control col-12 inputBorder mt-1'}),
            'additional_booklet': forms.Select(attrs={'class': 'form-control col-12 inputBorder mt-1'}),

            #3C
            'religion_1': forms.TextInput(attrs={'class': 'form-control col-12 inputBorder '}), 
            'citizen_1': forms.Select(attrs={'class': 'form-control col-12 inputBorder mt-1', 'onchange': 'handle3CChange()'}),
            'other_country_1': forms.TextInput(attrs={'class': 'form-control col-12 inputBorder', 'readonly': 'readonly'}), 
            'ethnicity_1': forms.TextInput(attrs={'class': 'form-control col-12 inputBorder', 'readonly': 'readonly'}),
            'health_problem_a_1': forms.Select(attrs={'class': 'form-control col-12 inputBorder '}), 
            'health_problem_b_1': forms.Select(attrs={'class': 'form-control col-12 inputBorder '}), 
            'health_problem_c_1': forms.Select(attrs={'class': 'form-control col-12 inputBorder '}), 
            'health_problem_d_1': forms.Select(attrs={'class': 'form-control col-12 inputBorder'}), 
            'health_problem_e_1': forms.Select(attrs={'class': 'form-control col-12 inputBorder'}), 
            'health_problem_f_1': forms.Select(attrs={'class': 'form-control col-12 inputBorder'}), 
            'remarks_3C': forms.TextInput(attrs={'class': 'form-control col-12 inputBorder '}),

            #3D
            'province_time_birth_1': forms.TextInput(attrs={'class': 'form-control col-12 inputBorder ', 'placeholder': 'province'}), 
            'municipality_time_birth_1': forms.TextInput(attrs={'class': 'form-control col-12 inputBorder ', 'placeholder': 'municipality'}), 
            'province_reside_1': forms.TextInput(attrs={'class': 'form-control col-12 inputBorder ', 'placeholder': 'province'}), 
            'municipality_reside_1': forms.TextInput(attrs={'class': 'form-control col-12 inputBorder ', 'placeholder': 'municipality'}), 
            'read_write_1': forms.Select(attrs={'class': 'form-control col-12 inputBorder '}), 
            'highest_year_completed_1': forms.TextInput(attrs={'class': 'form-control col-12 inputBorder '}), 
            'attend_school_1': forms.Select(attrs={'class': 'form-control col-12 inputBorder ', 'onchange': 'handle3DChange()'}), 
            'province_school_attended_1': forms.TextInput(attrs={'class': 'form-control col-12 inputBorder ', 'placeholder': 'province', 'readonly': 'readonly'}),
            'municipality_school_attended_1': forms.TextInput(attrs={'class': 'form-control col-12 inputBorder ', 'placeholder': 'municipality', 'readonly': 'readonly'}),
            'overseas_worker_1': forms.Select(attrs={'class': 'form-control col-12 inputBorder '}), 

            #3E
            'usual_activity_1': forms.TextInput(attrs={'class': 'form-control col-12 inputBorder '}),
            'business_worked_1': forms.TextInput(attrs={'class': 'form-control col-12 inputBorder '}),
            'kind_of_worker_1': forms.TextInput(attrs={'class': 'form-control col-12 inputBorder '}),
            'province_work_past12months_1': forms.TextInput(attrs={'class': 'form-control col-12 inputBorder ','placeholder': 'province',}),
            'municipality_work_past12months_1': forms.TextInput(attrs={'class': 'form-control col-12 inputBorder ', 'placeholder': 'municipality'}),
            'children_borned_1': forms.TextInput(attrs={'class': 'form-control col-12 inputBorder ', 'oninput': 'handle3EChange()'}),
            'children_still_living_1': forms.TextInput(attrs={'class': 'form-control col-12 inputBorder ', 'readonly': 'readonly'}),
            'children_alive_specificdate_1': forms.TextInput(attrs={'class': 'form-control col-12 inputBorder ', 'readonly': 'readonly'}),
            'age_firstmarriage_1': forms.TextInput(attrs={'class': 'form-control col-12 inputBorder '}),
            'remarks_3E': forms.TextInput(attrs={'class': 'form-control col-12 inputBorder '}),
        }
       