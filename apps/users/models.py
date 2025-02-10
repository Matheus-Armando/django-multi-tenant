from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add any additional fields you want for your user model
    tenant_id = models.CharField(max_length=100)

    def __str__(self):
        return self.username