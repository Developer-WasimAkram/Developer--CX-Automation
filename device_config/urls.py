
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static



from .views import device_config,download_file
urlpatterns = [
    path("device_config/",device_config, name='device_config' ),
    path('downloads/',download_file,name='downloads'),
    
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
