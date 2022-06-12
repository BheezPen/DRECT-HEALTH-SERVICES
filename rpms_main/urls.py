from django.urls import path
from . import views
from .views import DashboardView, DashboardDetailView

app_name = 'main'
urlpatterns = [
    path('dashboard', DashboardView.as_view(), name="dashboard"),
    path('<int:pk>', DashboardDetailView.as_view(), name="detail")
]
