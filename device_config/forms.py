from django import forms
from .models import DeviceConfiguration
class  DeviceConfigurationForm(forms.Form):
    
    class Meta:
        model=DeviceConfiguration
        fields=['host','username','password','file']