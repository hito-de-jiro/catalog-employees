from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from rest_framework import viewsets

from .forms import LoginForm, RegisterForm, UpdateUserForm
from .models import Employee
from .serializers import EmployeeSerializer


def home(request):
    return render(request, 'catalog/home.html')


@login_required
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


class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'registration/register.html'

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='/')

        return render(request, self.template_name, {'form': form})


class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='user-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)

    return render(request, 'registration/profile.html', {'user_form': user_form})
