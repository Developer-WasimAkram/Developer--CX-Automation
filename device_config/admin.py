from django.contrib import admin
from .models import DeviceConfiguration

# Register your models here.
@admin.register(DeviceConfiguration)
class DeviceConfigurationAdmin(admin.ModelAdmin):
    list_display = ('host', 'username', 'password','file')