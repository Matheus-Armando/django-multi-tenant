from django.urls import path, include

urlpatterns = [
    path('users/', include('apps.users.urls')),
    # Add other app URLs here
]