


# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

#from Rest.api.serializers import TiendaSerializer
#from Rest.api.serializers import ProductoSerializer

from Rest.models import sucursal, cliente, factura
from Rest.models import productos

#class Tienda(APIView):
 #   serializer_class=TiendaSerializer
  #  serializer_class=ProductoSerializer
   # def get(self, request, format=None):

#        tiendas= sucursal.objects.all()
 #       producto=productos.objects.all()

#        response=self.serializer_class(sucursal,many=True)
 #       return Response(response.data)
#tien=Tienda.as_view()

from Rest.models import sucursal
from rest_framework import viewsets
from .serializers import sucursalSerializer, productoSerializer, clienteSerializer, facturaSerializer


class SucursalViewSet(viewsets.ModelViewSet):
    queryset = sucursal.objects.all()
    serializer_class=sucursalSerializer
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = productos.objects.all()
    serializer_class = productoSerializer
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = cliente.objects.all()
    serializer_class =clienteSerializer
class FacturaViewSet(viewsets.ModelViewSet):
    queryset = factura.objects.all()
    serializer_class = facturaSerializer

