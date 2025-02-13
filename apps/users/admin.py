from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'is_tenant_owner', 'tenant']
    list_filter = ['is_tenant_owner', 'tenant', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        ('Tenant Information', {'fields': ('tenant', 'is_tenant_owner')}),
    )