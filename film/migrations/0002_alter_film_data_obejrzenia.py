# Generated by Django 3.2.8 on 2021-12-01 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='data_obejrzenia',
            field=models.DateField(),
        ),
    ]
