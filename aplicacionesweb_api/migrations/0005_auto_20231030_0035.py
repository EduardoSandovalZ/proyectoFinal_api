# Generated by Django 2.2 on 2023-10-30 00:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacionesweb_api', '0004_materia_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materia',
            name='usuario',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
