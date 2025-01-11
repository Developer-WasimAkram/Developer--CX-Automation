
from django.contrib import admin
from django.urls import path,include
from .views import user_login,user_signup,dashboard,log_out
from django.contrib.auth import views as auth_views
urlpatterns = [
    path("login/",user_login,name='login' ),
    path('register/',user_signup,name='register'),
    path('dashboard/',dashboard,name='dashboard'),
    path('logout/',log_out,name='logout'),
    
    # Password reset URLs
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    
]