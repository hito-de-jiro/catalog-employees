from django.shortcuts import render

from .models import Employee


def employee_hierarchy(request):
    employees = Employee.objects.all()
    return render(request, 'catalog/employees.html', {'employees': employees})
