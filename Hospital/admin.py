from django.contrib import admin

from Hospital.models import Doctor
from .models import Doctor,Patient,Appointment

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)

