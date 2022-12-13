from django.contrib import admin
from .models import usuario
# Register your models here.

class AdminUsuario(admin.ModelAdmin):
    class Meta:
        model=usuario


admin.site.register(usuario)

# Register your models here.
