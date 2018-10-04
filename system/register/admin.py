from django.contrib import admin
from .models import Personas, Empresas, Sucursales, Operadores, Buses, Comprobantes, Lectores, Lineas, Movimientos, Tarjetas, Timbrados, TipoBuses, TipoPago, TipoTarjeta, Trayectos

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

class SucursalAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'lector', 'nombre', 'direccion', 'contacto')
    search_fields = ['id_empresas', 'nombre']

    def empresa(self,obj):
        return obj.id_empresas
    
    def lector(self, obj):
        return obj.id_lectores

class BusesAdmin(admin.ModelAdmin):
    list_display = ('Tipo_de_Bus', 'empresa', 'trayecto', 'operador', 'lector', 'linea', 'chapa', 'coche_numero', 'observaciones')
    search_fields = ['empresa', 'trayecto', 'operador', 'lector', 'linea', 'chapa', 'coche_numero', 'observaciones']

    def Tipo_de_Bus(self, obj):
        return obj.id_tipo_buses

    def empresa(self,obj):
        return obj.id_empresas

    def trayecto(self,obj):
        return obj.id_trayectos

    def operador(self,obj):
        return obj.id_operadores

    def lector(self,obj):
        return obj.id_lectores

    def linea(self,obj):
        return obj.id_lineas

class TrayectoAdmin(admin.ModelAdmin):
    list_display = ('ramal', 'itinerario_ida', 'itinerario_vuelta', )
    search_fields = ['ramal', 'itinerario_ida', 'itinerario_vuelta',]

class ComprobanteAdmin(admin.ModelAdmin):
    list_display = ('timbrado', 'factura_numero', 'lector', 'movimiento', 'fecha', )

    def timbrado(self, obj):
        return obj.id_timbrados

    def factura_numero(self, obj):
        return obj.num_doc

    def lector(self,obj):
        return obj.id_lectores

    def movimiento(self,obj):
        return obj.id_mov

class LectorAdmin(admin.ModelAdmin):
    list_display = ('serie', 'Estado', )
    search_fields = ['serie']

    def Estado (self, obj):
        if obj.estado == 1:
            return 'Activo'
        else:
            return 'Inactivo'
        
class TimbradoAdmin(admin.ModelAdmin):
    list_display = ('numero', 'valido_desde', 'valido_hasta', 'factura_inicio', 'factura_fin', 'Estado', )
    search_fields = ['numero']

    def factura_inicio(self, obj):
        return obj.num_doc_ini

    def factura_fin(self, obj):
        return obj.num_doc_fin

    def Estado (self, obj):
            if obj.estado == 1:
                return 'Activo'
            else:
                return 'Inactivo'

class TarjetaAdmin(admin.ModelAdmin):
    list_display = ('uid', 'fecha_expedicion', 'fecha_vencimiento', 'Estado', 'saldo_actual', 'id_tipo_tarjetas', )

    def Estado (self, obj):
            if obj.estado == 1:
                return 'Activo'
            else:
                return 'Inactivo'


admin.site.site_title = 'Panel'
admin.site.index_title = 'Panel Principal'
admin.site.site_header = 'XBUS' 
admin.site.site_url = None
admin.site.register(Personas, PersonaAdmin)
admin.site.register(Empresas, EmpresaAdmin)
admin.site.register(Operadores, OperadorAdmin)
admin.site.register(Buses, BusesAdmin)
admin.site.register(Comprobantes, ComprobanteAdmin)
admin.site.register(Lectores, LectorAdmin)
admin.site.register(Lineas)
admin.site.register(Movimientos)
admin.site.register(Sucursales, SucursalAdmin)
admin.site.register(Tarjetas, TarjetaAdmin)
admin.site.register(Timbrados, TimbradoAdmin)
admin.site.register(TipoBuses)
admin.site.register(TipoPago)
admin.site.register(TipoTarjeta)
admin.site.register(Trayectos, TrayectoAdmin)

