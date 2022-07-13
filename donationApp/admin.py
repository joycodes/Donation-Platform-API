from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


# Register your models here.

admin.site.register(Charity)
admin.site.register(Donor)
admin.site.register(Donations)
admin.site.register(Feedback)
admin.site.register(Posts)
admin.site.register(User, UserAdmin)
admin.site.register(Beneficiary)
# admin.site.register(AnonymousDonation)