# Generated by Django 3.2.8 on 2021-11-09 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_monthgoal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tomeet',
            name='phone_number',
            field=models.CharField(max_length=12),
        ),
    ]
