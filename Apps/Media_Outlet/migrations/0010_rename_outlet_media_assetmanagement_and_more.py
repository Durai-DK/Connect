# Generated by Django 4.1.7 on 2023-02-23 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Media_Outlet', '0009_alter_showroom_details_address'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Outlet_Media',
            new_name='AssetManagement',
        ),
        migrations.AlterModelOptions(
            name='ad_status',
            options={'verbose_name_plural': 'AD Status'},
        ),
        migrations.AlterModelOptions(
            name='assetmanagement',
            options={'verbose_name_plural': 'Asset Management'},
        ),
        migrations.AlterModelOptions(
            name='brand_location',
            options={'verbose_name_plural': 'Brand Location'},
        ),
        migrations.AlterModelOptions(
            name='brand_type',
            options={'verbose_name_plural': 'Brand type'},
        ),
        migrations.AlterModelOptions(
            name='class_details',
            options={'verbose_name_plural': 'class Management'},
        ),
        migrations.AlterModelOptions(
            name='floor_diagram',
            options={'verbose_name_plural': 'Floor Diagram'},
        ),
        migrations.AlterModelOptions(
            name='full_img',
            options={'verbose_name_plural': '360 Degree Image'},
        ),
        migrations.AlterModelOptions(
            name='light_type',
            options={'verbose_name_plural': 'Light Type'},
        ),
        migrations.AlterModelOptions(
            name='material_type',
            options={'verbose_name_plural': 'Material Type'},
        ),
        migrations.AlterModelOptions(
            name='showroom_details',
            options={'verbose_name_plural': 'Showroom Details'},
        ),
        migrations.AlterModelTable(
            name='assetmanagement',
            table='AssetManagement',
        ),
    ]
