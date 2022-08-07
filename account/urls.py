from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as acc
from account import views


urlpatterns = [
    path('login/', acc.LoginView.as_view(), name='login'),
    path('logout/', acc.LogoutView.as_view(), name='logout'),

    path('password_change/', acc.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', acc.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password_reset/', acc.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', acc.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', acc.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', acc.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('register/', views.register, name='register'),

    path('', views.dashboard, name='dashboard'),
    path('edit/', views.edit, name='edit'),

]
