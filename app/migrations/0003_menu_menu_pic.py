# Generated by Django 3.2 on 2021-08-03 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_categoria_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='menu_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
