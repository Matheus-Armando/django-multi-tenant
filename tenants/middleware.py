# middleware.py

from django.utils.deprecation import MiddlewareMixin
from tenants.models import Tenant

class TenantMiddleware(MiddlewareMixin):
    def process_request(self, request):
        subdomain = request.META['HTTP_HOST'].split('.')[0]
        try:
            request.tenant = Tenant.objects.get(subdomain=subdomain)
        except Tenant.DoesNotExist:
            request.tenant = None