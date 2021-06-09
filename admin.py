from django.contrib import admin
from .models import *
from diagnosticcentre.models import Contact
# Register your models here.


admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Contact)
admin.site.register(Appointment)