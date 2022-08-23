from email.mime import application
from optparse import Option
from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=10)

class User2(models.Model):
    name = models.CharField(max_length=10)

# Association table for User
    
class GI_Association_regestration(models.Model):
    
    Appli_num = models.AutoField(primary_key=True)
    name_of_applicant = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    persons_products_organization_authority = models.CharField(max_length=100)
    type_of_goods = models.CharField(max_length=100)
    specification = models.CharField(max_length=100)
    name_of_geographical_indications = models.CharField(max_length=100)
    desc_of_goods = models.CharField(max_length=100)
    geo_area = models.FloatField(max_length=100)
    proof_of_origin = models.CharField(max_length=100)
    method_of_production = models.CharField(max_length=100)
    uniqueness = models.CharField(max_length=100)
    inspection_body =  models.CharField(max_length=100)
    other = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    is_deleted = models.BooleanField(default=False)
    form_type = models.CharField(max_length=20)
    date_of_regestration = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name_of_applicant

'''class GI_Assoctiation_renewal(models.Model):
    renewal_num = models.AutoField(primary_key=True)
    name_of_applicant = models.CharField(max_length=100)

    def __str__(self):
        return self.name_of_applicant '''

#public tables for user 

class GI_Association_application_status(models.Model):
    application_id = models.AutoField(primary_key=True)
    assoc_id = models.ForeignKey(GI_Association_regestration, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    ph_num = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.user_name
    
    class Meta:
        verbose_name_plural = "GI_Association_application_status"


#user table
class GI_User_reges(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    address_of_user = models.CharField(max_length=100)
    email_id = models.CharField(max_length=100)
    ph_num = models.CharField(max_length=100)
    Association_number = models.ForeignKey(GI_Association_regestration, on_delete=models.CASCADE)
    gi_number = models.CharField(max_length=100)
    date_of_registration = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "User Registration"
    
    def __str__(self):
        return self.user_name

class GI_User_application_status(models.Model):
    user = models.ForeignKey(GI_User_reges, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add=True) 

    def __str__(self):
        return self.status 
    class Meta:
        verbose_name_plural = "User Application Status"
class GI_User_renual(models.Model):
    application_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(GI_User_reges, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    ph_num = models.CharField(max_length=100)


    def __str__(self):
        return self.user_name
         

#django user login authentication
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    #additional attributes
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username
