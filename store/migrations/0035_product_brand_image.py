# Generated by Django 3.1.5 on 2021-03-21 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0034_auto_20210320_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand_image',
            field=models.ImageField(default='productImages/defaultProductImage.jpg', upload_to='brandImages'),
        ),
    ]
