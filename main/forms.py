from django import forms

class Form1(forms.Form):

    appli_num = forms.CharField(label='Application Number', max_length=100)
    name_of_applicant = forms.CharField(label='Name of Applicant', max_length=100)
    address = forms.CharField(label='Address', max_length=100)
    persons_products_organization_authority = forms.CharField(label='Persons, Products, Organization, Authority', max_length=100)
    type_of_goods = forms.CharField(label='Type of Goods', max_length=100)
    specification = forms.CharField(label='Specification', max_length=100)
    name_of_geographical_indications = forms.CharField(label='Name of Geographical Indications', max_length=100)
    desc_of_goods = forms.CharField(label='Description of Goods', max_length=100)
    geo_area = forms.CharField(label='Geographical Area', max_length=100)
    proof_of_origin = forms.CharField(label='Proof of Origin', max_length=100)
    method_of_production = forms.CharField(label='Method of Production', max_length=100)
    uniqueness = forms.CharField(label='Uniqueness', max_length=100)
    inspection_body = forms.CharField(label='Inspection Body', max_length=100)
    other = forms.CharField(label='Other', max_length=100)
        
#jkssbdkb
