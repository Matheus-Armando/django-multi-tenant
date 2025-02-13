from django.db import models
from django_tenants.models import TenantMixin
from django.conf import settings

class Tenant(TenantMixin):
    name = models.CharField(max_length=100)
    schema_name = models.CharField(max_length=63, unique=True)
    domain_url = models.CharField(max_length=128, unique=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='owned_tenants'
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    auto_create_schema = True

    class Meta:
        verbose_name = 'tenant'
        verbose_name_plural = 'tenants'

    def __str__(self):
        return self.name