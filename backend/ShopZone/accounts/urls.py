from django.urls import path
from .views import LoginView, RegisterAdminView, RegisterCustomerView

urlpatterns = [
    path('register-admin/', RegisterAdminView.as_view(), name='register-admin'),
    path('register-customer/', RegisterCustomerView.as_view(), name='register-customer'),
    path('login-admin/', LoginView.as_view(), name='login-admin'),
    path('login-customer/', LoginView.as_view(), name='login-customer')
]