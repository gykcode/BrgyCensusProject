from django.shortcuts import render
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .forms import CensusForm
from .models import CensusFormModel
from django import forms

# Create your views here.
@login_required(login_url="/login/")
def index(request):
    return render(request, 'home/index.html')

def forms(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CensusForm(request.POST)
        if form.is_valid():
            # Process the form data
            enumeration_area_number = form.cleaned_data['enumeration_area_number']
            building_serial = form.cleaned_data['building_serial']
            housing_unit_serial_number = form.cleaned_data['housing_unit_serial_number']
            line_number_respondents = form.cleaned_data['line_number_respondents']
            last_name = form.cleaned_data['last_name']
            first_name = form.cleaned_data['first_name']
            address = form.cleaned_data['address']

            # Render the template with the form inputs
            return render(request, 'home/forms.html', {
                'enumeration_area_number': enumeration_area_number, 
                'building_serial': building_serial,
                'housing_unit_serial_number': housing_unit_serial_number,
                'line_number_respondents': line_number_respondents,
                'last_name': last_name,
                'first_name': first_name,
                'address': address,
            })

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CensusForm()
    print('test')
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
