# Generated by Django 3.2.6 on 2021-08-31 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barber', '0005_alter_cita_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita',
            name='estado',
            field=models.CharField(blank=True, choices=[('P', 'Pagada'), ('C', 'Cancelada'), ('A', 'Activa')], default='A', max_length=1, null=True, verbose_name='Estado'),
        ),
    ]
