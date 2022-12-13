from django.urls import path
from .import views



from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
   path("administrador/", views.administrador, name="administrador"),
   path("portafolio/", views.portafolio, name="portafolio"),
   path("agregar/", views.agregar, name="agregar"),
   path("actualizar/", views.actualizar, name="actualizar"),
   path("eliminar/<int:id>", views.eliminar, name="eliminar"),
   path("actualizar/<int:id>", views.actualizar, name="actualizar"),
   path("ayuda/", views.ayuda, name="ayuda"),
   path("ayudaCliente/", views.ayudaCliente, name="ayudaCliente"),
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


