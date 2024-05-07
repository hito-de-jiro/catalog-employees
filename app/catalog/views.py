from django.shortcuts import render
from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer

from django.http import JsonResponse


def index(request):
    return render(request, 'catalog/index.html')


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


def employee_list(request):
    employees = Employee.objects.all().order_by('id')
    return render(request, template_name='catalog/employees.html', context={'employees': employees})
