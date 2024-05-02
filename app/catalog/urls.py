from django.urls import path
from .views import (
    index,
    employee_list,
)

urlpatterns = [
    path('', index, name='index'),  # http://127.0.0.1:8000/catalog/
    path('employees/', employee_list, name='employees'),  # http://127.0.0.1:8000/catalog/employees/
]
