from time import time
from django.db import models
from django.conf import settings
 

User = settings.AUTH_USER_MODEL

class Doctor(models.Model):
    person = models.ForeignKey(User, related_name = "doctor", on_delete=models.CASCADE)
    is_a_doctor = models.BooleanField(default=False)
    appointments = models.ManyToManyField('Appointments', related_name="appointments")
    hourly_fee = models.PositiveIntegerField()
    patients_treated = models.PositiveIntegerField()
    about = models.TextField()
    fields_of_expertise = models.CharField(max_length=200)


    def __str__(self):
        return str(self.person)

class Patient(models.Model):
    person = models.ForeignKey(User, related_name="patient", on_delete=models.CASCADE)
    is_a_patient = models.BooleanField(default=True)
    appointment = models.ForeignKey('Appointments', related_name = "patient_appointment", on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.person)

class Appointments(models.Model):
    user = models.ForeignKey(User, related_name = "patient_appointment", on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, related_name = "doctor_appointment", on_delete=models.CASCADE)
    time = models.DateTimeField()
    complaint = models.TextField(null=True)
    is_discharged = models.BooleanField(default=False)


    def __str__(self):
        return str(self.user)


    class Meta:
        verbose_name_plural = "Appointment"


class PreviousVisits(models.Model):
    patient = models.ForeignKey(User, related_name = "patient_visit", on_delete=models.CASCADE)
    time_of_visit = models.ForeignKey(Appointments, related_name="time_of_visits", on_delete=models.CASCADE)
    number_of_visits = models.PositiveIntegerField(null=True)

    @property
    def name(self):
        return self.time_of_visit.time

    @property
    def count_visits():
        if Appointments.is_discharged == True:
            return PreviousVisits.number_of_visits + 1
        else:
            return PreviousVisits.number_of_visits