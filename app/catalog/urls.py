from django.urls import path
from .views import employee_hierarchy, employee_list

urlpatterns = [
    path('employee_hierarchy/', employee_hierarchy, name='employee_hierarchy'),  # http://127.0.0.1:8000/catalog/employee_hierarchy/
    path('employees/', employee_list, name='employee_list'),  # http://127.0.0.1:8000/catalog/employees/
]
