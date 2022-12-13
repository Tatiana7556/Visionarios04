from django.urls import path
from .import views

urlpatterns = [
    path("productos/",views.productos, name="productos"),
    path("lg/",views.producto_LG, name="lg"),
    path("mabe/",views.producto_mabe, name="lg"),
    path("challenger/",views.producto_challenger, name="challenger"),
    path("abba/",views.producto_abba, name="abba"),
    path("whirlpool/",views.producto_whirpool, name="whirlpool"),
    path("televisores/",views.televisor, name="televisores"),
    path("electrodomesticos/",views.electrodomestico, name="electrodomesticos"),
    path("equipoSonido/",views.equipoSonido, name="equipoSonido"),
    path('compras/', views.compras,name='compras'),
    path('cotizacion/', views.cotizacion,name='cotizacion'),
    path('gracias/', views.gracias,name='gracias'),
    path('eliminar_cotizacion/<int:id>', views.eliminar_cotizacion,name='eliminar_cotizacion'),
    
  
   
]
    
    