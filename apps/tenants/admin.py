from django.contrib import admin
from .models import Tenant

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ['name', 'schema_name', 'domain_url', 'owner', 'created_on']
    search_fields = ['name', 'schema_name', 'domain_url']
    list_filter = ['created_on']
    readonly_fields = ['created_on', 'updated_on']