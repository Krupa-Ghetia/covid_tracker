from django.db import models
from datetime import datetime


class UserProfile(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    phone = models.CharField(max_length=10, null=False, blank=False)
    zip_code = models.CharField(max_length=10, null=False, blank=False)
    is_admin = models.BooleanField(default=False)
    row_created = models.DateTimeField(default=datetime.now)
    row_last_updated = models.DateTimeField(default=datetime.now)