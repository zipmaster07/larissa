# Generated by Django 4.2.3 on 2023-08-04 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoring', '0018_alter_score_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firearm',
            name='manufacturer',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='firearm',
            name='model',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
