from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    fields = (
        "name",
        "email",
        "phone",
        "department",
        "designation",
        "salary",
        "joining_date",
        "address",
        "is_active",
    )