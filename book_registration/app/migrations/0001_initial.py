# Generated by Django 3.2.5 on 2021-07-08 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('genere', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=100)),
                ('image', models.ImageField(default='default.jpg', upload_to='book_image')),
            ],
        ),
    ]
