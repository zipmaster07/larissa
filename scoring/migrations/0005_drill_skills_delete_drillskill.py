# Generated by Django 4.2.3 on 2023-07-31 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoring', '0004_remove_drill_skill_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='drill',
            name='skills',
            field=models.ManyToManyField(to='scoring.skill'),
        ),
        migrations.DeleteModel(
            name='DrillSkill',
        ),
    ]
