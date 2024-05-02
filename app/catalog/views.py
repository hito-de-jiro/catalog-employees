from django.shortcuts import render

from .models import Employee


def index(request):
    return render(request, 'catalog/index.html')


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, template_name='catalog/employees.html', context={'employees': employees})
