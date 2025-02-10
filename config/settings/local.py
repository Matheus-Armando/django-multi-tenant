from .base import *
import environ

BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT', default='5432'),
        'OPTIONS': {
            'sslmode': 'require' 
        }
    }
}

# Multi-tenant settings
MIDDLEWARE = [
    'django_tenant_schemas.middleware.TenantMiddleware',
    # ...other middleware
]

DATABASE_ROUTERS = (
    'django_tenant_schemas.routers.TenantSyncRouter',
)

# # Tenant Model
# TENANT_MODEL = "clients.Client"  # We'll create this model
AUTH_USER_MODEL = 'users.User'

# Shared Apps (available to all tenants)
SHARED_APPS = (
    'django_tenant_schemas',
    'apps.clients',  # app containing tenant model
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

# Tenant Apps (isolated per tenant)
TENANT_APPS = (
    'apps.users',
    # other tenant-specific apps
)

INSTALLED_APPS = list(SHARED_APPS) + [app for app in TENANT_APPS if app not in SHARED_APPS]