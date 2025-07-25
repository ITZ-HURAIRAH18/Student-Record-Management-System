from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Login and Logout views
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Password change views
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(template_name='changep.html'), name='password_change'),
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='changepdone.html'), name='password_change_done'),
    
    # Password reset views
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(template_name='preset.html'), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='presetdone.html'), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='Cpass.html'), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='Compass.html'), name='password_reset_complete'),

    # App-specific URLs
    path('', include('app.urls')),  # Replace 'app' with your app name
]
