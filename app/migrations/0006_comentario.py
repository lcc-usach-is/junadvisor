# Generated by Django 3.2 on 2021-08-15 00:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_estudiante'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.CharField(max_length=500, null=True)),
                ('calificacion', models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('is_active', models.BooleanField(default=True)),
                ('estudiante', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.estudiante')),
                ('menu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.menu')),
            ],
        ),
    ]
