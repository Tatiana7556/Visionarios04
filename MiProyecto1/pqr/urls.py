from django.urls import path
from .import views

urlpatterns = [
  path('pqr/', views.pqr, name='pqr'),
  path('contact/', views.contact, name='contact'),
  

]