from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from rest_framework import viewsets

from .forms import LoginForm
from .models import Employee
from .serializers import EmployeeSerializer


def index(request):
    # server side / ajax
    return render(request, 'catalog/index.html')


class EmployeeViewSet(viewsets.ModelViewSet, LoginRequiredMixin):
    # API - DRF
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


@login_required
def employee_list(request):
    # django processing
    employees = Employee.objects.all().order_by('id')
    return render(request, template_name='catalog/employees.html', context={'employees': employees})


@login_required
def employee_data(request):
    # return JSON data
    employees = Employee.objects.all()
    data = []
    for employee in employees:
        manager_name = employee.manager.full_name if employee.manager else None
        data.append({
            'full_name': employee.full_name,
            'position': employee.position,
            'hire_date': employee.hire_date,
            'salary': employee.salary,
            'manager': manager_name
        })
    return JsonResponse(data, safe=False)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('catalog')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login! Try again!')

    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})
