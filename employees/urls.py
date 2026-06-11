from django.urls import path
from .views import EmployeeListCreateView, EmployeeDetailView, employee_page

urlpatterns = [
    # Dashboard
    path("", employee_page, name="employee-page"),

    # API
    path("api/", EmployeeListCreateView.as_view(), name="employee-list"),
    path("api/<int:pk>/", EmployeeDetailView.as_view(), name="employee-detail"),
]