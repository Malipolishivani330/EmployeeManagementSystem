from django.db.models import Avg, Max, Q
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics, filters
from rest_framework.permissions import BasePermission, SAFE_METHODS
from django_filters.rest_framework import DjangoFilterBackend

from .models import Employee
from .serializers import EmployeeSerializer


# Home Page
def home(request):
    return employee_page(request)


# Employee Dashboard Page
def employee_page(request):
    search = request.GET.get("search", "")

    # Get all employees
    employees = Employee.objects.all()

    # Search by multiple fields
    if search:
        employees = employees.filter(
            Q(name__icontains=search)
            | Q(email__icontains=search)
            | Q(phone__icontains=search)
            | Q(department__icontains=search)
            | Q(designation__icontains=search)
        )

    # Dashboard Statistics
    total_employees = Employee.objects.count()

    total_departments = (
        Employee.objects.values("department")
        .distinct()
        .count()
    )

    highest_salary = (
        Employee.objects.aggregate(Max("salary"))["salary__max"]
        or 0
    )

    average_salary = (
        Employee.objects.aggregate(Avg("salary"))["salary__avg"]
        or 0
    )

    active_employees = Employee.objects.filter(
        is_active=True
    ).count()

    inactive_employees = Employee.objects.filter(
        is_active=False
    ).count()

    return render(
        request,
        "employees/employee_list.html",
        {
            "employees": employees,
            "search": search,
            "total_employees": total_employees,
            "total_departments": total_departments,
            "highest_salary": highest_salary,
            "average_salary": round(average_salary, 2),
            "active_employees": active_employees,
            "inactive_employees": inactive_employees,
        },
    )


# Custom Permission
class IsAdminOrReadOnly(BasePermission):

    def has_permission(self, request, view):

        if request.method in SAFE_METHODS:
            return True

        return request.user and request.user.is_staff


# Employee List & Create API
class EmployeeListCreateView(generics.ListCreateAPIView):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAdminOrReadOnly]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = [
        "department",
        "is_active",
    ]

    search_fields = [
        "name",
        "email",
        "phone",
        "department",
        "designation",
    ]

    ordering_fields = [
        "salary",
        "name",
        "joining_date",
    ]

    ordering = ["name"]


# Employee Detail API
class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAdminOrReadOnly]
