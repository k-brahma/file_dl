# Generated by Django 4.1.6 on 2023-02-06 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dl', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadfile',
            name='serial_number',
            field=models.CharField(default='a', max_length=100, unique=True, verbose_name='製造番号'),
        ),
    ]
