from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username",]

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(GIAssociatationRegistrationModel)
#admin.site.register(GI_Assoctiation_renewal)
admin.site.register(GI_User_reges)
admin.site.register(GI_User_renual)
admin.site.register(GI_Association_application_status)
admin.site.register(GI_User_application_status)








