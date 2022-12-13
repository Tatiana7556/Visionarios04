from django.shortcuts import render,redirect
from .models import compra
from .models import  catalogo,LG,mabe,challenger,abba,whirlpool,televisores,electrodomesticos,sonido
from django.db.models import Q
from .forms import CompraForm
from django.contrib import messages

def productos(request): 
    queryset= request.GET.get("buscar")
    catalogos=catalogo.objects.filter()
    if queryset:
        catalogos=catalogo.objects.filter(
            Q(nombre__icontains=queryset)|
            Q(descripcion__icontains=queryset)
        ).distinct()
    
    context={
        'catalogos':catalogos,
    }
    return render(request,'productos.html', context)


def producto_LG(request):
    lgs=LG.objects.all()
    context={
        'lgs':lgs,
    }
    return render(request,'LG.html',context)

def producto_mabe(request):
    mabes=mabe.objects.all()
    context={
        'mabes':mabes,
    }
    return render(request,'mabe.html',context)

def producto_challenger(request):
    ch=challenger.objects.all()
    context={
        'ch':ch
    }  
    return render(request,'challenger.html',context)  

def producto_abba(request):
    abbas=abba.objects.all()
    context={
        'abbas':abbas
    }
    return render(request,'abba.html',context) 

def producto_whirpool(request):
    wh=whirlpool.objects.all()
    context={
        'wh':wh
    }
    return render(request,'whirlpool.html',context)  

def televisor(request):
    televisor=televisores.objects.all()
    context={
        'televisor':televisor
    }
    return render(request,'televisores.html',context)  

def electrodomestico(request):
    elec=electrodomesticos.objects.all()
    context={
        'elec':elec
    }
    return render(request,'electrodomesticos.html',context)  

def equipoSonido(request):
    so=sonido.objects.all()
    context={
        'so':so
    }
    return render(request,'equipoSonido.html',context)   

def compras(request):
    formulario=CompraForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('gracias')
    return render(request,'formulario_compra.html',{'formulario':formulario})

def cotizacion(request):
    cotizaciones=compra.objects.all()
    return render(request,'cotizaciones.html',{'cotizaciones':cotizaciones}) 

def eliminar_cotizacion(request,id):
    cotizaciones= compra.objects.get(id=id)
    cotizaciones.delete()
    messages.success(request,'Se Cancelo Correctamente La Cotizacion.')
    return redirect('cotizacion')     

def gracias(request):
    return render(request,'gracias.html')

 