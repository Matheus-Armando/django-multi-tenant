def get_tenant_from_request(request):
    """
    Utility function to retrieve the tenant from the request.
    Assumes that the tenant is determined from the subdomain.
    """
    subdomain = request.get_host().split('.')[0]
    try:
        tenant = Tenant.objects.get(subdomain=subdomain)
        return tenant
    except Tenant.DoesNotExist:
        return None

def create_tenant(subdomain, name, schema_name):
    """
    Utility function to create a new tenant.
    """
    tenant = Tenant(subdomain=subdomain, name=name, schema_name=schema_name)
    tenant.save()
    return tenant

def delete_tenant(tenant):
    """
    Utility function to delete a tenant.
    """
    tenant.delete()