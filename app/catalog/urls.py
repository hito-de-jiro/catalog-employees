from django.urls import path, include
from rest_framework import routers
from .views import (
    index,
    employee_list,
    EmployeeViewSet
)

router = routers.DefaultRouter()
router.register(r'employee', EmployeeViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('employees/', employee_list, name='employees'),  # http://127.0.0.1:8000/catalog/employees/
    path('', index, name='employee'),  # http://127.0.0.1:8000/catalog/
]
