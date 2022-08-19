from django.urls import path

from . import views

urlpatterns = [
    path('main', views.home),
    path('about/', views.about),
    path('registration', views.registration),
    path('renewal', views.renewal),
    path('contact', views.contact),
    path('faq', views.faq),
    #path('login', views.login),
    path("GI_Associatation_RegistrationForm/<form_type>", views.GI_Association_regestration, name="GI_Association_regestration"),
    path("GI_Associatation_RenewalForm/", views.GI_association_renewal, name="GI_association_renewal"),
    path("GI_User_RegistrationForm", views.GI_user_registration, name="GI_user_registration"),
    path("GI_User_RenewalForm", views.GI_user_renewal, name="GI_user_renewal"),


]