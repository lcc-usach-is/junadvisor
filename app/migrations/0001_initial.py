# Generated by Django 3.2 on 2021-08-03 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comercio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, null=True)),
                ('descripcion', models.CharField(max_length=500, null=True)),
                ('direccion', models.CharField(max_length=100, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, null=True)),
                ('precio', models.PositiveIntegerField()),
                ('descripcion', models.CharField(max_length=500, null=True)),
                ('calificacion_media', models.FloatField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('categoria', models.ManyToManyField(to='app.Categoria')),
                ('comercio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.comercio')),
            ],
        ),
    ]
