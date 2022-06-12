from django.contrib import admin

from .models import Appointments, Doctor, Patient, PreviousVisits

admin.site.register(Appointments)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(PreviousVisits)