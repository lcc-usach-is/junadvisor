# Generated by Django 3.2 on 2021-08-18 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default-profile-pic.png', null=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='Recomendacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, null=True)),
                ('contenido', models.CharField(max_length=500, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('estudiante', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.estudiante')),
            ],
        ),
    ]