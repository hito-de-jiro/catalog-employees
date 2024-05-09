from django.urls import path, include
from django.contrib.auth import views as auth_views

from rest_framework import routers

from .forms import LoginForm
from .views import (
    index,
    employee_list,
    EmployeeViewSet,
    employee_data,
    RegisterView,
    CustomLoginView,
    profile, home,
)

router = routers.DefaultRouter()
router.register(r'employee', EmployeeViewSet)

urlpatterns = [
    path('employees/', employee_list, name='employees'),  # http://127.0.0.1:8000/employees/
    path('employee-data/', employee_data, name='employee_data'),  # http://127.0.0.1:8000/catalog/employee-data/
    path('catalog/', index, name='catalog'),  # http://127.0.0.1:8000/catalog/
    path('api/', include(router.urls)),

    path('', home, name='home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='registration/login.html',
                                           authentication_form=LoginForm), name='user-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='user-logout'),
    path('profile/', profile, name='user-profile'),
]
