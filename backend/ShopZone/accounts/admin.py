from django.contrib import admin
from .models import CustomUser

class UserAccountAdmin(admin.ModelAdmin):
    list_display = ['email', 'password', 'is_staff']



admin.site.register(CustomUser, UserAccountAdmin)
