# Generated by Django 3.2.5 on 2021-07-21 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210720_1716'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='patyment_id',
            new_name='payment_id',
        ),
    ]