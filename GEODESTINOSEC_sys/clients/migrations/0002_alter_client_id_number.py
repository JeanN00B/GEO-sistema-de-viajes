# Generated by Django 5.0.2 on 2024-03-26 13:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='id_number',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(code='nomatch', message='Error ID/RUC/Pasaporte no válido!', regex='(^\\d{10}|^[a-zA-Z0-9]*)$')]),
        ),
    ]
