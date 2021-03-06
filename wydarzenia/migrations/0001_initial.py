# Generated by Django 3.2.9 on 2022-01-04 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('data_wydarzenia', models.DateField()),
                ('miejsce', models.CharField(max_length=255)),
                ('osoby', models.CharField(max_length=500)),
                ('rodzaj', models.PositiveSmallIntegerField(choices=[(0, 'Prywatne'), (1, 'zawodowe')], default=0)),
            ],
        ),
    ]
