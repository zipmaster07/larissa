# Generated by Django 4.2.3 on 2023-08-03 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoring', '0009_alter_string_dummy_round_count_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='stringdistance',
            name='unique_string_distance',
        ),
        migrations.RenameField(
            model_name='stringdistance',
            old_name='distance',
            new_name='starting_distance',
        ),
        migrations.AddField(
            model_name='stringdistance',
            name='ending_distance',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddConstraint(
            model_name='stringdistance',
            constraint=models.UniqueConstraint(fields=('string', 'starting_distance', 'distance_type'), name='unique_string_distance'),
        ),
    ]
