# Generated by Django 3.1.5 on 2021-03-20 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0024_auto_20210320_0643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='last_name',
        ),
    ]
