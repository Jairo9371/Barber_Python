from django.db import models

# Create your models here.

class Cliente(models.Model):
    ''' Modelo para guardar Clientes '''
    identificador = models.AutoField(primary_key = True, verbose_name = 'Id')
    nombre = models.CharField(max_length = 150, blank = False, null = False, verbose_name = 'Nombre')
    apellido = models.CharField(max_length = 150, blank = True, null = True, verbose_name = 'Apellido')
    direccion = models.CharField(max_length = 100, blank = False, null = False, verbose_name = 'Dirección')
    telefono = models.IntegerField(blank = False, null = False, verbose_name = 'Telefono')

    def __str__(self):
        return '{} - {}'.format(self.nombre, self.direccion)

    class Meta:
        verbose_name_plural = 'Clientes'

class Barbero(models.Model):
    ''' Modelo para guardar Barberos '''

    identificador = models.AutoField(primary_key = True, verbose_name = 'Id')
    nombre = models.CharField(max_length = 150, blank = False, null = False, verbose_name = 'Nombre')
    apellido = models.CharField(max_length = 150, blank = True, null = True, verbose_name = 'Apellido')
    telefono = models.IntegerField(blank = False, null = False, verbose_name = 'Telefono')

    def __str__(self):
        return '{} - {}'.format(self.nombre, self.telefono)

    class Meta:
        verbose_name_plural = 'Barberos'

class Horario(models.Model):
    ''' Modelo para guardar Horarios '''

    identificador = models.AutoField(primary_key = True, verbose_name = 'Id')
    hora = models.TimeField(auto_now=False, auto_now_add=False, verbose_name = "Hora")

    def __str__(self):
        return '{}'.format(self.hora)
    
    class Meta:
        verbose_name_plural = 'hora'

class Tarifa(models.Model):
    ''' Modelo para guardar Tarifas '''

    identificador = models.AutoField(primary_key = True, verbose_name = 'Id')
    tipo = models.CharField(max_length = 25, blank = False, null = False, verbose_name = 'Tipo')
    precio = models.DecimalField(max_digits = 12, decimal_places = 2, verbose_name = 'Precio')

    def __str__(self):
        return '{} - {}'.format(self.tipo, self.precio)
    
    class Meta:
        verbose_name_plural = 'Tarifas'

class Cita(models.Model):
    ''' Modelo para guardar Citas '''

    ACTIVA = 'A'
    CANCELADA = 'C'
    PAGADA = 'P'

    ESTADO_CITA = {
        (ACTIVA,'Activa'),
        (CANCELADA, 'Cancelada'),
        (PAGADA, 'Pagada')
    }

    identificador = models.AutoField(primary_key = True, verbose_name = 'Id')
    total = models.DecimalField(max_digits = 12, decimal_places = 2, verbose_name = 'Total')
    estado = models.CharField(max_length = 1, default = ACTIVA, null = True, blank = True, choices = ESTADO_CITA,  verbose_name = 'Estado' )
    cliente_id = models.ForeignKey(Cliente, on_delete = models.PROTECT, verbose_name = 'Cliente')
    horario_id = models.ForeignKey(Horario, on_delete = models.PROTECT, verbose_name = 'Horario')
    barbero_id = models.ForeignKey(Barbero, on_delete = models.PROTECT, verbose_name = 'Barbero')


    def __str__(self):
        return '{} - {}'.format(self.cliente_id, self.horario_id)
    
    class Meta:
        verbose_name_plural = 'Citas'

class Detalle_Cita(models.Model):
    ''' Modelo para guardar Detalle Citas '''

    identificador = models.AutoField(primary_key = True, verbose_name ='Id')
    subtotal = models.DecimalField(max_digits = 12, decimal_places = 2, verbose_name = 'Subtotal')
    cita_id = models.ForeignKey(Cita, on_delete = models.PROTECT, verbose_name = 'Cita')
    tarifa_id = models.ForeignKey(Tarifa, on_delete = models.PROTECT, verbose_name = 'Tarifas')

    def __str__(self):
        return '{} - {}'.format(self.tarifa_id, self.subtotal)
    
    class Meta:
        verbose_name_plural = 'Detalle de Citas'
        verbose_name = 'Detalle de Citas'

class Factura(models.Model):
    """Modelo para guardar las facturas que hace la Barberia"""

    identificador = models.AutoField(primary_key=True, verbose_name = 'Id')
    no_serie = models.CharField(max_length = 15, default= "A", blank = False, null = False, verbose_name = 'No. Serie')
    fecha = models.DateField(auto_now = False, auto_now_add = False, verbose_name = 'Fecha de la Factura')
    descripcion = models.CharField(max_length = 500, blank = False, null = False, verbose_name = 'Descripción')
    total = models.DecimalField(max_digits = 12, decimal_places = 2, verbose_name = 'Total')
    cita_id = models.ForeignKey(Cita, on_delete = models.PROTECT, verbose_name = 'Cita')

    def __str__(self):
        return '{} - {}'.format(self.no_serie, self.total)
    
    class Meta:
        verbose_name_plural = 'Facturas'

