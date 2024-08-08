# Generated by Django 4.2.15 on 2024-08-08 08:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('A', 'arrendatario'), ('B', 'arrendador')], default='A', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=9, unique=True)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=12)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Inmueble',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_inmueble', models.CharField(choices=[('A', 'terreno'), ('B', 'edificio'), ('C', 'casa')], max_length=60)),
                ('nombre_inmueble', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('m2_construido', models.FloatField()),
                ('numero_banos', models.IntegerField(default=0)),
                ('numero_habitaciones', models.IntegerField(default=0)),
                ('direccion', models.CharField(max_length=100)),
                ('id_usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='arrienda_ya.usuario')),
            ],
        ),
    ]
