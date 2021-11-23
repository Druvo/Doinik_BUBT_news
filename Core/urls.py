from django.urls import path
from django.contrib.auth import views as auth_views

from Core import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path(
        'password_reset/', auth_views.PasswordResetView.as_view(
            template_name="password_reset_form.html"
        ), name='password_reset'
    ),
    path(
        'password_reset/done/', auth_views.PasswordResetDoneView.as_view(
            template_name="password_reset_done.html"
        ), name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
            template_name="password_reset_confirm.html"
        ), name='password_reset_confirm'
    ),
    path(
        'reset/done/', auth_views.PasswordResetCompleteView.as_view(
            template_name="password_reset_complete.html"
        ), name='password_reset_complete'
    ),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('registration/', views.Registration.as_view(), name='registration'),
]
