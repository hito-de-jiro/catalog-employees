from django.urls import path, include
from rest_framework import routers
from .views import (
    index,
    employee_list,
    EmployeeViewSet,
    employee_data,
    user_login,
)

router = routers.DefaultRouter()
router.register(r'employee', EmployeeViewSet)

urlpatterns = [
    path('employees/', employee_list, name='employees'),  # http://127.0.0.1:8000/catalog/employees/
    path('employee-data/', employee_data, name='employee_data'),  # http://127.0.0.1:8000/catalog/employee-data/
    path('catalog/', index, name='catalog'),  # http://127.0.0.1:8000/catalog/
    path('api/', include(router.urls)),
    path('', user_login, name='login'),
]
