from django.db import models

# Create your models here.

class DeviceConfiguration(models.Model):
    host = models.CharField(max_length=30)
    username = models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    file=models.FileField()