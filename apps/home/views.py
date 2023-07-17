from django.shortcuts import render
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .forms import CensusForm
from django.views import View
from django.http import JsonResponse

# Create your views here.
@login_required(login_url="/login/")
def index(request):
    return render(request, 'home/index.html')

@login_required(login_url="/login/")
def create_forms(request):
    # if this is a POST request we need to process the form data
    
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CensusForm(request.POST)
        # print(form,'kjhkjhjgjhgfghgfhhjkjhkjhjhj')
        if form.is_valid():
            # Process the form data
            # 3A
            enumeration_area_number = form.cleaned_data['enumeration_area_number']
            building_serial = form.cleaned_data['building_serial']
            housing_unit_serial_number = form.cleaned_data['housing_unit_serial_number']
            household_serial_number = form.cleaned_data['household_serial_number']
            line_number_respondents = form.cleaned_data['line_number_respondents']
            last_name = form.cleaned_data['last_name']
            first_name = form.cleaned_data['first_name']
            address = form.cleaned_data['address']

            date_time_created_1 = form.cleaned_data['date_time_created_1']
            date_time_ended_1 = form.cleaned_data['date_time_ended_1']
            result_1 = form.cleaned_data['result_1']
            result_description_1 = form.cleaned_data['result_description_1']

            date_time_created_2 = form.cleaned_data['date_time_created_2']
            date_time_ended_2 = form.cleaned_data['date_time_ended_2']
            result_2 = form.cleaned_data['result_2']
            result_description_2 = form.cleaned_data['result_description_2']

            date_time_created_3 = form.cleaned_data['date_time_created_3']
            date_time_ended_3 = form.cleaned_data['date_time_ended_3']
            result_3 = form.cleaned_data['result_3']
            result_description_3 = form.cleaned_data['result_description_3']

            appointment_date_time_1 = form.cleaned_data['appointment_date_time_1']
            appointment_date_time_2 = form.cleaned_data['appointment_date_time_2']
            appointment_date_time_3 = form.cleaned_data['appointment_date_time_3']

            number_of_visit = form.cleaned_data['number_of_visit']
            result_of_final_visit = form.cleaned_data['result_of_final_visit']
            number_of_household_member = form.cleaned_data['number_of_household_member']
            number_male = form.cleaned_data['number_male']
            number_female = form.cleaned_data['number_female']
            enumerator_code = form.cleaned_data['enumerator_code']
            mode_of_data_collection = form.cleaned_data['mode_of_data_collection']

            # 3B
            residing_fullname_1 = form.cleaned_data['residing_fullname_1']
            relationship_to_head_1 = form.cleaned_data['relationship_to_head_1']
            gender_1 = form.cleaned_data['gender_1']
            date_born_1 = form.cleaned_data['date_born_1']
            age_1 = form.cleaned_data['age_1']
            birth_registered_1 = form.cleaned_data['birth_registered_1']
            copy_birthcert_1 = form.cleaned_data['copy_birthcert_1']
            marital_status_1 = form.cleaned_data['marital_status_1']
            not_yet_listed = form.cleaned_data['not_yet_listed']
            additional_booklet = form.cleaned_data['additional_booklet']

            #3C
            religion_1 = form.cleaned_data['religion_1']
            citizen_1 = form.cleaned_data['citizen_1']
            other_country_1 = form.cleaned_data['other_country_1']
            ethnicity_1 = form.cleaned_data['ethnicity_1']
            health_problem_a_1 = form.cleaned_data['health_problem_a_1']
            health_problem_b_1 = form.cleaned_data['health_problem_b_1']
            health_problem_c_1 = form.cleaned_data['health_problem_c_1']
            health_problem_d_1 = form.cleaned_data['health_problem_d_1']
            health_problem_e_1 = form.cleaned_data['health_problem_e_1']
            health_problem_f_1 = form.cleaned_data['health_problem_f_1']
            



            #saving the input fields into the model
            form.save()

            #resetting to blank forms after clicking submit
            form = CensusForm()
    # if a GET (or any other method) we'll create a blank form
    else:
        form = CensusForm()

    return render(request, 'home/forms.html', {'form': form})





@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
