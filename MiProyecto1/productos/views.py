from django.shortcuts import render, redirect
from .models import producto
from .forms import productoForm
from django.db.models import Q
from django.contrib import messages




# Create your views here.


def administrador(request):
    return render (request,'administrador.html')

def portafolio(request):
    queryset= request.GET.get("buscar")
    productos= producto.objects.filter()
    if queryset:
        productos=producto.objects.filter(
            Q(nombre__icontains=queryset)|
            Q(descripcion__icontains=queryset)
        ).distinct()    
    context={
        'productos':productos,
    }  
    return render (request,'portafolio.html', context)    

def agregar(request):
    formulario=productoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request,'Se Creo Correctamente el Producto.') 
        return redirect ('portafolio')
    return render (request,'Agregar.Producto.html' , {'formulario':formulario}) 

def actualizar(request, id):
    productos=producto.objects.get(id=id)
    formulario=productoForm(request.POST or None, request.FILES or None, instance=productos)
    if formulario.is_valid() and request.POST:
        formulario.save()
        messages.success(request,'Se Actualizo Correctamente el Producto.') 
        return redirect ('portafolio')
    return render (request,'actualizar.html',{'formulario':formulario})       

def eliminar(request,id):
    productos= producto.objects.get(id=id)
    productos.delete()
    messages.success(request,'Se Elimino Correctamente el Producto.') 
    return redirect('portafolio')
     
def ayuda(request):
    return render(request, 'Ayuda_administrador.html')

def ayudaCliente(request):
    return render(request,'ayuda_usuario.html')