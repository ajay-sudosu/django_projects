# Generated by Django 3.2.5 on 2021-07-04 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.AddField(
            model_name='review',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]