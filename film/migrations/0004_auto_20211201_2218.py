# Generated by Django 3.2.9 on 2021-12-01 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0003_auto_20211201_2002'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='film',
            options={'verbose_name': 'film', 'verbose_name_plural': 'filmy'},
        ),
        migrations.AlterUniqueTogether(
            name='film',
            unique_together={('title', 'rok_produkcji')},
        ),
    ]
