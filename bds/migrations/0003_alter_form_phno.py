# Generated by Django 4.1.3 on 2022-12-01 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bds', '0002_form'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='phno',
            field=models.BigIntegerField(),
        ),
    ]
