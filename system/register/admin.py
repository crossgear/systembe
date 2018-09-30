from django.contrib import admin
from .models import Personas, Empresas, Operadores, Buses, Caja, Comprobantes, Lectores, Lineas, Movimientos, Tarjetas, Timbrados, TipoBuses, TipoPago, TipoTarjeta, Trayectos

class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'cedula', 'telefono', 'celular', 'direccion', 'fecha_nacimiento')
    search_fields = ['nombres', 'apellidos', 'cedula', 'telefono', 'celular', 'direccion', 'fecha_nac']

    def fecha_nacimiento(self, obj):
        return obj.fecha_nac

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nombre_razon_social','ruc', 'telefono', 'celular', 'direccion', 'actividad_economica')
    search_fields = ['nombre_razon_social','ruc', 'telefono', 'celular', 'direccion', 'actividad_economica']
    
class OperadorAdmin(admin.ModelAdmin):
    list_filter = (
        ('id_empresas', admin.RelatedOnlyFieldListFilter),
    )
    list_per_page = 10
    list_display = ('nombres', 'Apellidos', 'Cedula', 'Telefono', 'Celular', 'Direccion', 'fecha_nacimiento', 'empresa')
    search_fields = ['nombres', 'apellidos', 'cedula', 'telefono', 'celular', 'direccion', 'fecha_nacimiento', 'empresa']

    def nombres(self, obj):
        return obj.id_personas

    def empresa(self, obj):
        return obj.id_empresas

    def Apellidos(self, obj):
        return obj.id_personas.apellidos

    def Cedula(self, obj):
        return obj.id_personas.cedula

    def Telefono(self, obj):
        return obj.id_personas.telefono

    def Celular(self, obj):
        return obj.id_personas.celular

    def Direccion(self, obj):
        return obj.id_personas.direccion

    def fecha_nacimiento(self, obj):
        return obj.id_personas.fecha_nac


admin.site.site_title = 'Panel'
admin.site.index_title = 'Panel Principal'
admin.site.site_header = 'XBUS'
admin.site.register(Personas, PersonaAdmin)
admin.site.register(Empresas, EmpresaAdmin)
admin.site.register(Operadores, OperadorAdmin)
admin.site.register(Buses)
admin.site.register(Caja)
admin.site.register(Comprobantes)
admin.site.register(Lectores)
admin.site.register(Lineas)
admin.site.register(Movimientos)
admin.site.register(Tarjetas)
admin.site.register(Timbrados)
admin.site.register(TipoBuses)
admin.site.register(TipoPago)
admin.site.register(TipoTarjeta)
admin.site.register(Trayectos)

