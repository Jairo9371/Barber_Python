from django.contrib import admin
from.models import *
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'direccion', 'telefono')
    search_fields = ('=identificador','nombre', 'apellido',)

class BarberoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'telefono')
    search_fields = ('=identificador','nombre', 'apellido',)

class HorarioAdmin(admin.ModelAdmin):
    list_display = ('hora',)

class TarifAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'precio')
    search_fields = ('=identificador','tipo')

class CitAdmin(admin.ModelAdmin):
    list_display = ('cliente_id', 'barbero_id', 'horario_id', 'total')

class Detalle_CitAdmin(admin.ModelAdmin):
    list_display = ('cita_id', 'tarifa_id', 'subtotal')

class FacturAdmin(admin.ModelAdmin):
    list_display = ('no_serie', 'fecha', 'descripcion', 'total')


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Barbero, BarberoAdmin)
admin.site.register(Horario, HorarioAdmin)
admin.site.register(Tarifa, TarifAdmin)
admin.site.register(Cita, CitAdmin)
admin.site.register(Detalle_Cita, Detalle_CitAdmin)
admin.site.register(Factura, FacturAdmin)
