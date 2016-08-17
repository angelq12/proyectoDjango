
from rest_framework.serializers import ModelSerializer

from Rest.models import sucursal, cliente, factura
#from Rest.models import productos

#class TiendaSerializer(ModelSerializer):
 #   class Meta:
  #      model=sucursal
 #       fields=('id','direccion','sigla','latitud','longitud')
#class ProductoSerializer(ModelSerializer):
 #   class Meta:
  #      model=productos
   #     fields=('id_productos','nombre_producto','precio','iva_producto')

from  Rest.models import (sucursal,productos)
from rest_framework import serializers

class sucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model=sucursal
        fields = ('id', 'direccion', 'sigla', 'latitud', 'longitud')
   # depth=1
class productoSerializer(serializers.ModelSerializer):
    class Meta:
        model=productos
        fields=('id_productos','nombre_producto','precio','iva_producto')
class clienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=cliente
        fields=('id_cliente','nombres','apellidos','cedula','correo','telefono','celular','direccion','genero','estadoCivil','fechaNacimiento')

class facturaSerializer(serializers.ModelSerializer):
    class Meta:
        model=factura
        fields=('id_facturas','num_factura','fecha_factura')