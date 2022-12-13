from django import forms
from .models import compra

class CompraForm(forms.ModelForm):
    class Meta:
       model=compra
       fields='__all__'
      

       