from django.urls import path

from .views import login_view, index
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name="index"),
    path('login/', login_view, name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="password/password-reset.html"), name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="password/password-reset-done.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password/password-reset-confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="password/password-reset-complete.html"), name='password_reset_complete'),
]
