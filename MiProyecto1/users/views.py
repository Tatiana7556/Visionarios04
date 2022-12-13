from django.shortcuts import render, redirect
from .forms import userRegisterForm
from django.contrib import messages


# Create your views here.
 
def incio(request):
    return render(request,"tatiana.html")


def registro(request):
    if request.method == 'POST':
        form= userRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Se ha registrado correctamente.')
            return redirect ('inicio')  
    else:
        form=userRegisterForm()
             
    context = {'form':form}
    return render(request,"Registro.html", context)    


