# Generated by Django 3.1.5 on 2021-04-25 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20210425_0136'),
    ]

    operations = [
        migrations.AddField(
            model_name='productreview',
            name='content',
            field=models.TextField(default=True),
            preserve_default=False,
        ),
    ]
