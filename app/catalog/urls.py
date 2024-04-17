from django.urls import path
from .views import employee_hierarchy

urlpatterns = [
    path('employee_hierarchy/', employee_hierarchy, name='employee_hierarchy'),  # http://127.0.0.1:8000/catalog/employee_hierarchy/
]
