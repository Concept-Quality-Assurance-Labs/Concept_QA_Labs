from django.db import models
import uuid

# Create your models here.

class Update1(models.Model):
    Info = models.CharField(max_length=600, null=True, blank=True)

class Update2(models.Model):
    Info = models.CharField(max_length=600, null=True, blank=True)

class Update3(models.Model):
    Info = models.CharField(max_length=600, null=True, blank=True)