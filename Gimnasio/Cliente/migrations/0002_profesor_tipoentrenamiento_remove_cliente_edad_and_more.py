# Generated by Django 5.0.4 on 2024-05-31 00:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('especialidad', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoEntrenamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='edad',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='fecha_registro',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='turno',
            name='cliente',
        ),
        migrations.AddField(
            model_name='cliente',
            name='direccion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='usuario',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='turno',
            name='usuario',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='turno',
            name='hora',
            field=models.TimeField(),
        ),
        migrations.AddField(
            model_name='turno',
            name='entrenamiento',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Cliente.tipoentrenamiento'),
        ),
    ]
