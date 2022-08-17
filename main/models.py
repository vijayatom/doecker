from email.mime import application
from optparse import Option
from statistics import mode
from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=10)
    
class GIGI1(models.Model):
    
    Appli_num = models.AutoField(primary_key=True)
    name_of_applicant = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    persons_products_organization_authority = models.CharField(max_length=100)
    type_of_goods = models.CharField(max_length=100)
    specification = models.CharField(max_length=100)
    name_of_geographical_indications = models.CharField(max_length=100)
    desc_of_goods = models.CharField(max_length=100)
    geo_area = models.CharField(max_length=100)
    proof_of_origin = models.CharField(max_length=100)
    method_of_production = models.CharField(max_length=100)
    uniqueness = models.CharField(max_length=100)
    inspection_body =  models.CharField(max_length=100)
    other = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    is_deleted = models.BooleanField(default=False)
    form_type = models.CharField(max_length=20)

    def __str__(self):
        return self.name_of_applicant
