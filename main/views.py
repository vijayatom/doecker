from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import Form1
import re

# Create your views here.

def index(request):
    Users = User.objects.all()
    context = {
        "Users":Users
    }
    return render(request,"index.html",context=context)

def create_form1(request, form_type):
    if form_type not in ['a','b','c','d']:
        return HttpResponse("Invalid form type")
    if request.method == 'POST':
        form = Form1(request.POST)
        if form.is_valid():
            
            data = form.cleaned_data
            form1 = GIGI1(
                name_of_applicant = data['name_of_applicant'],
                address = data['address'],
                persons_products_organization_authority = data['persons_products_organization_authority'],
                type_of_goods = data['type_of_goods'],
                specification = data['specification'],
                name_of_geographical_indications = data['name_of_geographical_indications'],
                desc_of_goods = data['desc_of_goods'],
                geo_area = data['geo_area'],
                proof_of_origin = data['proof_of_origin'],
                method_of_production = data['method_of_production'],
                uniqueness = data['uniqueness'],
                inspection_body = data['inspection_body'],
                other = data['other'],
                form_type = form_type
                
            )
            form1.save()
                
        '''      name_of_applicant = data['name_of_applicant'],
                address = data['address'],
                persons_products_organization_authority = data['persons_products_organization_authority'],
                type_of_goods = data['type_of_goods'],
                specification = data['specification'],
                name_of_geographical_indications = data['name_of_geographical_indications'],
                desc_of_goods = data['desc_of_goods'],
                geo_area = data['geo_area'],
                proof_of_origin = data['proof_of_origin'],
                method_of_production = data['method_of_production'],
                uniqueness = data['uniqueness'],
                inspection_body = data['inspection_body'],
                other = data['other'],
                form_type = form_type
                
            )'''
            #form.save()
        return HttpResponse("<h1>Form Submitted Successfully</h1>")
    return render(request,"form1.html", context={'form':Form1(request.GET)})

def home(request):
    return render(request, 'main.html')

def about(request):
    return render(request, 'about.html')
	
def registration(request):
	return render(request, 'registration.html')

def renewal(request):
    return render(request, 'renewal.html')
	
def contact(request):
	return render(request, 'contact.html')

