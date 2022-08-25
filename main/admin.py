from django.contrib import admin
from .models import User
from .models import *
# Register your models here.

admin.site.register(User)
admin.site.register(Gi_Associatation_registration)
#admin.site.register(GI_Assoctiation_renewal)
admin.site.register(GI_User_reges)
admin.site.register(GI_User_renual)
admin.site.register(GI_Association_application_status)
admin.site.register(GI_User_application_status)








