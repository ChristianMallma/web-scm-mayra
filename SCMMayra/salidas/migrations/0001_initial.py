# Generated by Django 2.0.2 on 2019-07-13 02:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('produccion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComprobanteDet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('cantidad', models.IntegerField(default=0)),
                ('precio', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
            ],
            options={
                'verbose_name': 'Detalle de comprobante',
                'verbose_name_plural': 'Detalle de comprobantes',
            },
        ),
        migrations.CreateModel(
            name='ComprobanteEnc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('fecha_factura', models.DateField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Encabezado de comprobante',
                'verbose_name_plural': 'Encabezado de comprobantes',
            },
        ),
        migrations.AddField(
            model_name='comprobantedet',
            name='comprobante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salidas.ComprobanteEnc'),
        ),
        migrations.AddField(
            model_name='comprobantedet',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produccion.Disenio'),
        ),
    ]
