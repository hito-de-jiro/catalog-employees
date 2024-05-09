from django.contrib.auth import views as auth_views
from django.urls import path, include
from rest_framework import routers

from .forms import LoginForm
from .views import (
    home,
    RegisterView,
    CustomLoginView,
    profile,

    index,
    employee_list,
    EmployeeViewSet,
    employee_data,
)

router = routers.DefaultRouter()
router.register(r'employee', EmployeeViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('register/', RegisterView.as_view(), name='user-register'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='registration/login.html',
                                           authentication_form=LoginForm), name='user-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='user-logout'),
    path('profile/', profile, name='user-profile'),

    path('employees/', employee_list, name='employees'),
    path('employee-data/', employee_data, name='employee_data'),
    path('catalog/', index, name='catalog'),

    path('api/', include(router.urls)),
]
