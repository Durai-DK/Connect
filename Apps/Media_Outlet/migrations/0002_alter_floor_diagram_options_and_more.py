# Generated by Django 4.0.4 on 2023-02-13 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Media_Outlet', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='floor_diagram',
            options={'verbose_name_plural': 'Floor_Diagram'},
        ),
        migrations.AlterModelTable(
            name='floor_diagram',
            table='Floor_Diagram',
        ),
    ]
