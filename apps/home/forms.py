from django import forms
from 

class CensusForm(forms.Form):
    first_name = forms.CharField(
        label='First Name',
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your first name',
            'class': 'form-control'
        })
    )
    last_name = forms.CharField(
        label='Last Name',
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your last name',
            'class': 'form-control'
        })
    )

    # Specify the template name
    template_name = 'home/forms.html'

# class CensusForm(forms.Form):
#     first_name = forms.CharField(label='First Name')
#     last_name = forms.CharField(label='Last Name')