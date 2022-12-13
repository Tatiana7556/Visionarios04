from django.urls import path
from .import views
from django.contrib.auth.views import LoginView , LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
   path("", views.incio, name="inicio"),
   path("registro/", views.registro, name="registro"),
   path('login/', LoginView.as_view(template_name='login.html'), name='login'),
   path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
   path('reset_password/', auth_views.PasswordResetView.as_view(template_name= 'password_resert_form.html'), name='password_reset'),
   path('reset_password_send/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
   path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
   path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'), 
]