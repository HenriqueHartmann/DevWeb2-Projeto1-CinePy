# Generated by Django 3.2.7 on 2021-10-08 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_cinema'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(unique=True)),
            ],
        ),
    ]
