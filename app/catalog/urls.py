from django.urls import path
from .views import (
    employee_list,
)

urlpatterns = [
    path('employees/', employee_list, name='employees'),  # http://127.0.0.1:8000/catalog/employees/
]
