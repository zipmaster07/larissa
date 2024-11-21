# Generated by Django 5.0.7 on 2024-11-21 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoring', '0026_caliber_unique_short_name_caliber'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='firearmdetails',
            constraint=models.UniqueConstraint(fields=('sight_type', 'suppressed', 'magazine_capacity'), name='unique_firearm_details'),
        ),
    ]
