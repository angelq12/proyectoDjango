from django.contrib import admin
from .models import sucursal, cliente
from .models import productos
from .models import factura
admin.site.register(sucursal)
admin.site.register(productos)
admin.site.register(cliente)
admin.site.register(factura)