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
    persons_products_organization_authority = forms.CharField(label='Persons, Products, Organization, Authority', max_length=100)
    type_of_goods = forms.CharField(label='Type of Goods', max_length=100)
    specification = forms.CharField(label='Specification', max_length=100)
    name_of_geographical_indications = forms.CharField(label='Name of Geographical Indications', max_length=100)
    desc_of_goods = forms.CharField(label='Description of Goods', max_length=100)
    geo_area = forms.FloatField(label='Geographical Area')
    file = forms.FileField()
    proof_of_origin = forms.CharField(label='Proof of Origin', max_length=100)
    method_of_production = forms.CharField(label='Method of Production', max_length=100)
    uniqueness = forms.CharField(label='Uniqueness', max_length=100)
    inspection_body = forms.CharField(label='Inspection Body', max_length=100)
    other = forms.CharField(label='Other', max_length=100)
    form_type= forms.CharField(label='Form Type?', widget=forms.Select(choices=FORM_TYPE_CHOICES))

'''class GI_Associatation_RenewalForm(forms.Form):
    name_of_applicant = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name of the applicant', 'style': 'width: 300px;', 'class': 'form-control'}))'''

class GI_User_RegistrationForm(forms.Form):
    user_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Full Name', 'style': 'width: 300px;', 'class': 'form-control'}))
    address_of_user = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Address', 'style': 'width: 300px;', 'class': 'form-control'}))
    email_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email Id', 'style': 'width: 300px;', 'class': 'form-control'}))
    ph_num = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone Number', 'style': 'width: 300px;', 'class': 'form-control'}))
    Association_number = forms.ModelChoiceField(queryset=GIAssociatationRegistrationModel.objects.all())


class GI_User_RenewalForm(forms.Form):
    user_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Full Name', 'style': 'width: 300px;', 'class': 'form-control'}))
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


