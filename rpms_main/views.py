
from django.http import HttpResponse
from .models import Doctor
from django.conf import settings

User = settings.AUTH_USER_MODEL


from django.views.generic import ListView, DetailView


class DashboardView(ListView):
    model = Doctor
    template = "rpms_main/templates/dashboard_list.html"

    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = super().get_queryset()
            doctor = Doctor.objects.filter(person=self.request.user)
            return doctor

class DashboardDetailView(DetailView):
    model = Doctor
    template_name = "templates/rpms_main/dashboard_detail.html"

    def get_query(self):
        if self.request.user.is_authenticated:
            doctor = Doctor.objects.filter(person=self.request.user)
            return doctor