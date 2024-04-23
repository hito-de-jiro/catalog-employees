from django.urls import path
from .views import employee_hierarchy, employee_list, employee_search, employee_data

urlpatterns = [
    path('employee_hierarchy/', employee_hierarchy, name='employee_hierarchy'),  # http://127.0.0.1:8000/catalog/employee_hierarchy/
    path('employees/', employee_list, name='employee_list'),  # http://127.0.0.1:8000/catalog/employees/
    path('employees/', employee_search, name='employee_search'),  # http://127.0.0.1:8000/catalog/employees/
    path('employees-data/', employee_data, name='employee_data'),  # http://127.0.0.1:8000/catalog/employees-data/
]
