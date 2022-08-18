from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('about', views.about),
    path('registration', views.registration),
    path('renewal', views.renewal),
    path('contact', views.contact),
    path("form1/<form_type>", views.create_form1, name="form1"),
    path('faq', views.faq),

]