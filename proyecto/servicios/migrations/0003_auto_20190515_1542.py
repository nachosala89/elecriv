# Generated by Django 2.0.5 on 2019-05-15 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0002_auto_20180705_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='estado',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('En curso', 'En curso'), ('Finalizado', 'Finalizado')], max_length=12),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='estado',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('En curso', 'En curso'), ('Finalizado', 'Finalizado')], max_length=1),
        ),
    ]
