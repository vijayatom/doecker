from django.urls import path

from . import views
from .views import SignUpView

urlpatterns = [
    path('main', views.home, name="home"),
    path("login", views.loginPage, name="login"),
    path("logout", views.logoutPage, name="logout"),
    path("signup", views.SignUpView.as_view(), name="signup"),
    path("test", views.CreateMyModelView.as_view(), name="test"),
    path("giassociationreg", views.Gi_Associatation_registration, name="Gi_Associatation_registration"),
    path("giassoapprove/<id>", views.update_gi_association, name="update_gi_association"),
    path("giassoverify/<id>", views.verify_gi_association, name="verify_gi_association"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("allassociations", views.allassociations, name="allassociations"),
    path("allusers", views.allusers, name="allusers"),

    path('about/', views.about),
    path('registration', views.registration),
    path('renewal', views.renewal),
    path('contact', views.contact),
    path('faq', views.faq),
    #path('login', views.login),
    #path("GI_Associatation_RenewalForm/", views.GI_association_renewal, name="GI_association_renewal"),
    path("GI_User_RegistrationForm", views.GI_user_registration, name="GI_user_registration"),
    path("GI_User_RenewalForm", views.GI_user_renewal, name="GI_user_renewal"),
    path("registration", views.registration, name="registration"),

]