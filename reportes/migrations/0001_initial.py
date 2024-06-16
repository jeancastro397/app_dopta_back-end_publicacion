# Generated by Django 5.0.6 on 2024-06-16 02:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('publicaciones', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ReporteEvento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.CharField(choices=[('SPAM', 'Spam'), ('INAPROPIADO', 'Contenido inapropiado'), ('FRAUDE', 'Contenido fraudulento'), ('OTRO', 'Otro')], max_length=20)),
                ('descripcion', models.TextField()),
                ('estado', models.CharField(choices=[('ACEPTADO', 'Aceptado'), ('EN REVISION', 'En revisión'), ('RECHAZADO', 'Rechazado')], default='EN REVISION', max_length=20)),
                ('fecha_reporte', models.DateTimeField(auto_now_add=True)),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publicaciones.evento')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Reportes de Eventos',
            },
        ),
        migrations.CreateModel(
            name='ReporteMascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.CharField(choices=[('SPAM', 'Spam'), ('INAPROPIADO', 'Contenido inapropiado'), ('FRAUDE', 'Contenido fraudulento'), ('OTRO', 'Otro')], max_length=20)),
                ('descripcion', models.TextField(max_length=255)),
                ('estado', models.CharField(choices=[('ACEPTADO', 'Aceptado'), ('EN REVISION', 'En revisión'), ('RECHAZADO', 'Rechazado')], default='EN REVISION', max_length=20)),
                ('fecha_reporte', models.DateTimeField(auto_now_add=True)),
                ('mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publicaciones.mascota')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Reportes de Mascotas',
            },
        ),
        migrations.CreateModel(
            name='ReporteServicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.CharField(choices=[('SPAM', 'Spam'), ('INAPROPIADO', 'Contenido inapropiado'), ('FRAUDE', 'Contenido fraudulento'), ('OTRO', 'Otro')], max_length=20)),
                ('descripcion', models.TextField()),
                ('estado', models.CharField(choices=[('ACEPTADO', 'Aceptado'), ('EN REVISION', 'En revisión'), ('RECHAZADO', 'Rechazado')], default='EN REVISION', max_length=20)),
                ('fecha_reporte', models.DateTimeField(auto_now_add=True)),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publicaciones.servicio')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Reportes de Servicios',
            },
        ),
    ]