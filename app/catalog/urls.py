from django.urls import path
from .views import employee_hierarchy

urlpatterns = [
    path('employee_hierarchy/', employee_hierarchy, name='employee_hierarchy'),
]
