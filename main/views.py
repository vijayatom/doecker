from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
import re
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from .functions import handle_uploaded_file  

# Create your views here.

def index(request):
    Users = User.objects.all()
    context = {
        "Users":Users
    }
    return render(request,"index.html",context=context)

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"

class CreateMyModelView(CreateView):
    model = GIAssociatationRegistrationModel
    form_class = MyModelForm
    template_name = 'test.html'
    success_url = 'test.html'

# Associatation Registration
def Gi_Associatation_registration(request):
    if request.method == 'POST':
        form = GI_Associatation_RegistionForm(request.POST, request.FILES)
        if form.is_valid():

            file_path = handle_uploaded_file(request.FILES['file'])  
            
            data = form.cleaned_data
            form = GIAssociatationRegistrationModel(
                user=request.user,
                name_of_applicant = data['name_of_applicant'],
                address = data['address'],
                persons_products_organization_authority = data['persons_products_organization_authority'],
                type_of_goods = data['type_of_goods'],
                specification = data['specification'],
                name_of_geographical_indications = data['name_of_geographical_indications'],
                desc_of_goods = data['desc_of_goods'],
                proof_of_origin = data['proof_of_origin'],
                method_of_production = data['method_of_production'],
                uniqueness = data['uniqueness'],
                inspection_body = data['inspection_body'],
                other = data['other'],
                form_type = data['form_type'],
                geo_area=file_path
                )
            form.save()

        return HttpResponse("<h1>Form Submitted Successfully</h1>")
    return render(request,"GI_Associatation_RegistrationForm.html",{'form':GI_Associatation_RegistionForm})



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
            )
            user.save()
        return HttpResponse("<h1>User Registration Successful</h1>")
    return render(request, 'GI_User_RegistrationForm.html', 
    context={'form':GI_User_RegistrationForm(request.GET)})

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
	

def renewal(request):
    return render(request, 'renewal.html')
	
def contact(request):
	return render(request, 'contact.html')

def logoutPage(request):
    print("calling")
    if request.user.is_authenticated:
        print("auth done")
        logout(request)
    return redirect('home')


def loginPage(request):
    if request.user.is_authenticated:
        print("auth done")
        return redirect('dashboard')
    else:
        if request.method == 'POST':    
            username = request.POST.get('username')
            password =request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Username OR password is incorrect')
        context = {}
        return render(request, 'login.html', context)

def register(request):
	return render(request, 'register.html')

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

def dashboard(request):

    if request.user.is_superuser:
        associations = GIAssociatationRegistrationModel.objects.all()
        context = {
            "associations":associations
        }
        return render(request, 'dashboard_officer.html', context=context)

    if request.user.is_association:
        associations = GIAssociatationRegistrationModel.objects.filter(user=request.user)
        context = {
            "associations":associations
        }
        return render(request, 'dashboard_association.html', context=context)
    else:
        return render(request, 'dashboard_user.html', context={})


def registration(request):
    return render(request,'registration.html')

def update_gi_association(request,id):
    print(id)
    t = GIAssociatationRegistrationModel.objects.get(application_number=id)
    t.status = 'approved'  # change field
    t.gi_tag = 'gti' + str(t.application_number)
    t.save() # this will update only
    return redirect('dashboard')

def verify_gi_association(request,id):
    print(id)
    t = GIAssociatationRegistrationModel.objects.get(application_number=id)
    t.status = 'verified'  # change field
    t.save() # this will update only
    return redirect('dashboard')
 

