from django.db import models

# Create your models here.
class sucursal(models.Model):
    id_sucursal=models.IntegerField()
    direccion=models.CharField(max_length=50)
    sigla=models.CharField(max_length=5)
    latitud=models.DecimalField(max_digits=19,decimal_places=15 )
    longitud=models.DecimalField(max_digits=19,decimal_places=15 )

    def __str__(self):
        return self.direccion
class productos(models.Model):
    id_productos=models.ForeignKey(sucursal,on_delete=models.CASCADE,default="")
    nombre_producto=models.CharField(max_length=30)
    precio=models.DecimalField(max_digits=5,decimal_places=2)
    iva_producto=models.DecimalField(max_digits=5,decimal_places=2)
    def __str__(self):
        return self.nombre_producto




class cliente(models.Model):
    listaGenero = (
        ('f', 'masculino'),
        ('m', 'femenino'),
    )
    listaEstadoCivil = (
        ('soltero', 'soltero'),
        ('casado', 'casado'),
        ('divorciado', 'divorciado'),
        ('viudo', 'viudo'),
    )
    id_cliente=models.ForeignKey(sucursal,on_delete=models.CASCADE,default="")
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    cedula = models.CharField(max_length=10)
    correo = models.EmailField(max_length=30, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    celular = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.TextField(max_length=50, default="direccion")
    genero = models.CharField(max_length=10, choices=listaGenero)
    estadoCivil = models.CharField(max_length=10, choices=listaEstadoCivil)
    fechaNacimiento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.cedula

class factura(models.Model):
    id_facturas = models.ForeignKey(cliente, on_delete=models.CASCADE, default="")
    num_factura = models.CharField(max_length=10)
    fecha_factura = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.num_factura