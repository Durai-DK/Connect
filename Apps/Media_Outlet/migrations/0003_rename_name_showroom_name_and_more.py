# Generated by Django 4.0.4 on 2023-02-13 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Media_Outlet', '0002_alter_floor_diagram_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='showroom',
            old_name='Name',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='outlet_media',
            name='AD_Image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
