# Generated by Django 3.2.8 on 2021-11-09 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_habits'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Habits',
            new_name='Habit',
        ),
    ]
