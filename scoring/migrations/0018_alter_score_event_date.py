# Generated by Django 4.2.3 on 2023-08-04 06:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoring', '0017_alter_history_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='event_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]