# Generated by Django 3.1.5 on 2021-03-18 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210317_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profileImages/defaultImg.jpg', upload_to='profileImages'),
        ),
    ]
