from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
import re
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# Create your views here.

def index(request):
    Users = User.objects.all()
    context = {
        "Users":Users
    }
    return render(request,"index.html",context=context)
# Associatation Registration
def Gi_Associatation_registration(request, form_type):
    if form_type not in ['a','b','c','d']:
        return HttpResponse("Invalid form type")
    if request.method == 'POST':
        form = GI_Associatation_RegistionForm(request.POST)
        if form.is_valid():
            
            data = form.cleaned_data
            form = GI_Association_regestration(
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
            form.save()
        return HttpResponse("<h1>Form Submitted Successfully</h1>")
    return render(request,"GI_Association_regestrationForm.html",{'form':GI_Associatation_RegistionForm})

#Associatation Renewal
'''def GI_association_renewal(request):
    if request .method == 'POST':
        form = GI_Associatation_RenewalForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form = GI_Assoctiation_renewal(
                name_of_applicant = data['name_of_applicant'],
                )
            form.save()
        return HttpResponse("<h1>Form Submitted Successfully</h1>")
    return render(request, 'GI_Associatation_RenewalForm.html', context={'form':GI_Associatation_RenewalForm(request.GET)})'''

# user Regesteration

def GI_user_registration(request):
    if request.method == 'POST':
        form = GI_User_RegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = GI_User_reges(
                user_name = data['user_name'],
                address_of_user = data['address_of_user'],
                email_id = data['email_id'],
                ph_num = data['ph_num'],
                Association_number = data['Association_number'],
                gi_number = data['gi_number'],
            )
            return HttpResponse("<h1>User Registration Successful</h1>")
    return render(request, 'GI_User_RegistrationForm.html', context={'form':GI_User_RegistrationForm(request.GET)})

# user renewal

def GI_user_renewal(request):
    if request.method == 'POST':
        form = GI_User_RenewalForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = GI_User_renual(
                user_name = data['user_name'],
                user_id = data['user_id'],
                ph_num = data['ph_num'],
            )
            return HttpResponse("<h1>User Renewal Successful</h1>")
    return render(request, 'GI_User_RenewalForm.html', context={'form':GI_User_RenewalForm(request.GET)})

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

def faq(request):
	return render(request, 'faq.html')   


# def form1(request):
# 	return render(request, 'form1.html')    

'''def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        form1 = userlogin(request.POST)
        data = form1.cleaned_data
        user = authenticate(username=data['username'], password=data['password'])
    
        if user:
            return HttpResponse("<h1>Login Successful</h1>")
        else:
            return HttpResponse("<h1>Login Failed</h1>")
    return render(request,"login.html", context={'form':userlogin(request.GET)})
    '''

def association_dashboard(request):
    # h = GI_Association_regestration.objects.prefetch_related('gi_association_application_status_set', 'gi_user_reges_set','gi_user_application_status').get(Appli_num='21')
    # print(h.gi_association_application_status_set.all())
    # print(h.gi_user_reges_set.all())
    # print(h.gi_user_application_status.all())
    h = GI_Association_regestration.objects.all()
    
    for i in h:
        print(i.user_name)
    # print(h)
    return render(request, 'dashboard1.html', context={'h':h})