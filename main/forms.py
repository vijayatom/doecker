from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import CustomUser, GIAssociatationRegistrationModel
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

FORM_TYPE_CHOICES= (
    ('a', 'Single Class'),
    ('b', 'Single Class Foreign Country'),
    ('c', 'Multiple Class'),
    ('d', 'Multiple Class Foreign Country'),
)

class MyModelForm(ModelForm):
    class Meta:
        model = GIAssociatationRegistrationModel
        fields = ('name_of_applicant','address', 'application_number',
        'persons_products_organization_authority','type_of_goods', 'specification',
        'name_of_geographical_indications', 'desc_of_goods', 'geo_area','proof_of_origin',
        'method_of_production','uniqueness','inspection_body','other','status','form_type','is_deleted')

class GI_Associatation_RegistionForm(forms.Form):
    #application_number = forms.CharField(label='Application Number', max_length=100)
    name_of_applicant = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name of the applicant', 'style': 'width: 300px;', 'class': 'form-control'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'address', 'style': 'width: 300px;', 'class': 'form-control'}))
    persons_products_organization_authority = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'persons / products / organization / authority', 'style': 'width: 300px;', 'class': 'form-control'}))
    type_of_goods = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type of Good', 'style': 'width: 300px;', 'class': 'form-control'}))
    specification = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Specification', 'style': 'width: 300px;', 'class': 'form-control'}))
    name_of_geographical_indications = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name of Geographical Indications', 'style': 'width: 300px;', 'class': 'form-control'}))
    desc_of_goods = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Description of goods', 'style': 'width: 300px;', 'class': 'form-control'}))
    geo_area = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': 'Geographical area', 'style': 'width: 300px;', 'class': 'form-control'}))
    file = forms.FileField()
    proof_of_origin = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Proof of Origin', 'style': 'width: 300px;', 'class': 'form-control'}))
    method_of_production = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Method of Production', 'style': 'width: 300px;', 'class': 'form-control'}))
    uniqueness = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Uniqueness', 'style': 'width: 300px;', 'class': 'form-control'}))
    inspection_body = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Inspection Body', 'style': 'width: 300px;', 'class': 'form-control'}))
    other = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Others', 'style': 'width: 300px;', 'class': 'form-control'}))
    form_type= forms.CharField(label='Form Type?', widget=forms.Select(choices=FORM_TYPE_CHOICES))

'''class GI_Associatation_RenewalForm(forms.Form):
    name_of_applicant = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name of the applicant', 'style': 'width: 300px;', 'class': 'form-control'}))'''

class GI_User_RegistrationForm(forms.Form):
    user_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'User Name', 'style': 'width: 300px;', 'class': 'form-control'}))
    address_of_user = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Address of the user', 'style': 'width: 300px;', 'class': 'form-control'}))
    email_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email Id', 'style': 'width: 300px;', 'class': 'form-control'}))
    ph_num = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone Number', 'style': 'width: 300px;', 'class': 'form-control'}))
    Association_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Association Number', 'style': 'width: 300px;', 'class': 'form-control'}))
    gi_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'GI Number', 'style': 'width: 300px;', 'class': 'form-control'}))


class GI_User_RenewalForm(forms.Form):
    user_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'User Name', 'style': 'width: 300px;', 'class': 'form-control'}))
    user_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'User Id', 'style': 'width: 300px;', 'class': 'form-control'}))
    ph_num = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone Number', 'style': 'width: 300px;', 'class': 'form-control'}))



class userlogin(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100)

class CreateCustomUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username','email','password1','password2', 'is_association')

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email", "first_name", "is_association")

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email")


