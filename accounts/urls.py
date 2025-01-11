
from django.contrib import admin
from django.urls import path,include
from .views import user_login,user_signup,dashboard,log_out

urlpatterns = [
    path("",user_login,name='login' ),
    path('register/',user_signup,name='register'),
    path('dashboard/',dashboard,name='dashboard'),
    path('logout/',log_out,name='logout')
    
    
]