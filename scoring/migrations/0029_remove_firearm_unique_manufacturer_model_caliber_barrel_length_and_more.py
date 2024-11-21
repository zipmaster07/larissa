# Generated by Django 5.0.7 on 2024-11-21 17:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoring', '0028_alter_firearm_barrel_length'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='firearm',
            name='unique_manufacturer_model_caliber_barrel_length',
        ),
        migrations.AlterField(
            model_name='firearm',
            name='firearm_details',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='scoring.firearmdetails'),
        ),
        migrations.AddConstraint(
            model_name='firearm',
            constraint=models.UniqueConstraint(fields=('manufacturer', 'model', 'caliber', 'barrel_length', 'firearm_details'), name='unique_manufacturer_model_caliber_barrel_length_firearm_details'),
        ),
    ]