from django.urls import path
from .views import LoginView, RegisterAdminView, RegisterCustomerView

urlpatterns = [
    path('accounts/register-admin/', RegisterAdminView.as_view(), name='register-admin'),
    path('accounts/register-customer/', RegisterCustomerView.as_view(), name='register-customer'),
    path('accounts/login-admin/', LoginView.as_view(), name='login-admin'),
    path('accounts/login-customer/', LoginView.as_view(), name='login-customer')
]