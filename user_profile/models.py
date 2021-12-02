from django.db import models
from datetime import datetime


class UserProfile(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    phoneNumber = models.CharField(max_length=10, null=False, blank=False, unique=True)
    pinCode = models.CharField(max_length=10, null=False, blank=False)
    row_created = models.DateTimeField(default=datetime.now)
    row_last_updated = models.DateTimeField(default=datetime.now)


class AdminProfile(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    phoneNumber = models.CharField(max_length=10, null=False, blank=False, unique=True)
    pinCode = models.CharField(max_length=10, null=False, blank=False)
    row_created = models.DateTimeField(default=datetime.now)
    row_last_updated = models.DateTimeField(default=datetime.now)