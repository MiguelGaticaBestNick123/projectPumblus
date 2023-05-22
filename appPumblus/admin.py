from django.contrib import admin
from .models import Pumblus, Carrito, Pedido, Staff, PumblusX

# Register your models here.

class PumblusAdmin(admin.ModelAdmin):
    list_display = ["idProducto", "nombre", "precio", "f_creacion", "f_caducidad"]
    list_editable = ["nombre", "precio", "f_creacion", "f_caducidad"]

    class meta:
        model = Pumblus


class PumblusXAdmin(admin.ModelAdmin):
    list_display = ["idProducto", "nombre", "precio", "largo_dingle_dop", "vibracion_floops", "grodus_inalambrico"]
    list_editable = ["nombre", "precio", "largo_dingle_dop", "vibracion_floops", "grodus_inalambrico"]

    class meta:
        model = PumblusX

class CarritoAdmin(admin.ModelAdmin):
    list_display = ["usuario", "pumblus", "cantidad"]
    list_editable = ["cantidad"]

    class meta:
        model = Carrito

class PedidoAdmin(admin.ModelAdmin):
    list_display = ["usuario", "fecha_creacion", "estado", "direccion_envio"]
    list_editable = ["estado", "direccion_envio"]
    
    class meta:
        model = Pedido

class StaffAdmin(admin.ModelAdmin):
    list_display = ["user", "nick", "cargo", "fecha_contratacion"]
    list_editable = ["nick", "cargo", "fecha_contratacion"]

    class meta:
        model = Staff

admin.site.register(Pumblus, PumblusAdmin)
admin.site.register(PumblusX, PumblusXAdmin)
admin.site.register(Carrito, CarritoAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Staff, StaffAdmin)
