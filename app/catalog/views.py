from django.shortcuts import render

from .models import Employee


def employee_hierarchy(request):
    employees = Employee.objects.all()
    return render(request, 'catalog/employees.html', {'employees': employees})


def employee_list(request):
    employees = Employee.objects.all()
    sort_by = request.GET.get('sort_by', 'full_name')
    employees = employees.order_by(sort_by)
    return render(request, 'catalog/employee_list.html', {'employees': employees})