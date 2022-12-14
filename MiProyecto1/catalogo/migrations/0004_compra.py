# Generated by Django 4.1.2 on 2022-12-03 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_catalogo_estado'),
    ]

    operations = [
        migrations.CreateModel(
            name='compra',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, null=True, verbose_name='nombre')),
                ('direccion', models.CharField(max_length=100, null=True, verbose_name='direccion')),
                ('telefono', models.CharField(max_length=15, null=True, verbose_name='telefono')),
                ('correo', models.EmailField(max_length=254, null=True, unique=True, verbose_name='correo')),
                ('pago', models.IntegerField(choices=[(1, 'Pago contra Entrega'), (2, 'Consignacion Bancaria')], default=1, verbose_name='pago')),
            ],
        ),
    ]
