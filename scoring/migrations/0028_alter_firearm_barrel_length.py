# Generated by Django 5.0.7 on 2024-11-21 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoring', '0027_firearmdetails_unique_firearm_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firearm',
            name='barrel_length',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]
