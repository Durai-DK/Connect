# Generated by Django 4.0.4 on 2023-02-15 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Media_Outlet', '0008_alter_showroom_details_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showroom_details',
            name='Address',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]