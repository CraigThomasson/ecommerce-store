# Generated by Django 3.2 on 2022-07-10 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_product_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='colour',
            field=models.CharField(default='white', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='scent',
            field=models.CharField(default='unscented', max_length=100),
        ),
    ]
