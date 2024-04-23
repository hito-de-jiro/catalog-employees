from django.db.models import Q
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


def employee_search(request):
    employees = Employee.objects.all()
    search_query = request.GET.get('search_query')
    if search_query:
        employees = employees.filter(
            Q(full_name__icontains=search_query) |
            Q(hire_date__icontains=search_query) |
            Q(salary__icontains=search_query)
        )
    return render(request, 'catalog/employee_list.html', {'employees': employees})


def employee_data(request):
    employees = Employee.objects.all()

    return render(request, 'catalog/employee-data.html', {'employees': employees})
