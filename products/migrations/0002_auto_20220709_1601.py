# Generated by Django 3.2 on 2022-07-09 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='placeholder', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.URLField(blank=True, default='placeholder', max_length=1024, null=True),
        ),
    ]
