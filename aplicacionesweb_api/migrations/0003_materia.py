# Generated by Django 2.2 on 2023-10-29 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacionesweb_api', '0002_auto_20231006_0339'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nrc', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=255)),
                ('seccion', models.CharField(max_length=10)),
                ('dias', models.CharField(max_length=50)),
                ('hora_inicio', models.TimeField()),
                ('hora_final', models.TimeField()),
                ('salon', models.CharField(max_length=20)),
                ('programa_educativo', models.CharField(max_length=255)),
            ],
        ),
    ]
