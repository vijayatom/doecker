from django.urls import path

from . import views

urlpatterns = [
    path('main', views.home, name="home"),
    path("login", views.loginPage, name="login"),
    path('about/', views.about),
    path('registration', views.registration),
    path('renewal', views.renewal),
    path('contact', views.contact),
    path('faq', views.faq),
    #path('login', views.login),
    path("giassreg/<form_type>", views.Gi_Associatation_registration, name="Gi_Associatation_registration"),
    #path("GI_Associatation_RenewalForm/", views.GI_association_renewal, name="GI_association_renewal"),
    path("GI_User_RegistrationForm", views.GI_user_registration, name="GI_user_registration"),
    path("GI_User_RenewalForm", views.GI_user_renewal, name="GI_user_renewal"),
    path("dashboard", views.dashboard1, name="dashboard"),
    path("assregister", views.assregister, name="assregister"),
    path("registration", views.registration, name="registration"),


]