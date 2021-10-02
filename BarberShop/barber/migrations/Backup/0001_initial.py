# Generated by Django 3.2.6 on 2021-08-28 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barbero',
            fields=[
                ('identificador', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('nombre', models.CharField(max_length=150, verbose_name='Nombre')),
                ('telefono', models.IntegerField(verbose_name='Telefono')),
            ],
            options={
                'verbose_name_plural': 'Barberos',
            },
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('identificador', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('total', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Total')),
                ('estado', models.CharField(blank=True, choices=[('P', 'Pagada'), ('C', 'Cancelada'), ('A', 'Activa')], default='A', max_length=1, null=True, verbose_name='Estado')),
                ('barbero_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='barber.barbero', verbose_name='Barbero')),
            ],
            options={
                'verbose_name': 'Citas',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('identificador', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('nombre', models.CharField(max_length=150, verbose_name='Nombre')),
                ('direccion', models.CharField(max_length=100, verbose_name='Dirección')),
                ('telefono', models.IntegerField(verbose_name='Telefono')),
            ],
            options={
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('identificador', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('hora', models.TimeField(verbose_name='Hora')),
            ],
            options={
                'verbose_name_plural': 'hora',
            },
        ),
        migrations.CreateModel(
            name='Tarifa',
            fields=[
                ('identificador', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('tipo', models.CharField(max_length=25, verbose_name='Tipo')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Precio')),
            ],
            options={
                'verbose_name_plural': 'Tarifas',
            },
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('identificador', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('no_serie', models.CharField(default='A', max_length=15, verbose_name='No. Serie')),
                ('fecha', models.DateField(verbose_name='Fecha de la Factura')),
                ('descripcion', models.CharField(max_length=500, verbose_name='Descripción')),
                ('total', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Total')),
                ('cita_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='barber.cita', verbose_name='Cita')),
            ],
            options={
                'verbose_name_plural': 'Facturas',
            },
        ),
        migrations.CreateModel(
            name='Detalle_Cita',
            fields=[
                ('identificador', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Subtotal')),
                ('cita_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='barber.cita', verbose_name='Cita')),
                ('tarifa_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='barber.tarifa', verbose_name='Tarifas')),
            ],
            options={
                'verbose_name': 'Detalle de Citas',
                'verbose_name_plural': 'Detalle de Citas',
            },
        ),
        migrations.AddField(
            model_name='cita',
            name='cliente_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='barber.cliente', verbose_name='Cliente'),
        ),
        migrations.AddField(
            model_name='cita',
            name='horario_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='barber.horario', verbose_name='Horario'),
        ),
    ]