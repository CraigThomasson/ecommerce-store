# Generated by Django 3.2 on 2022-07-22 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-added_on']},
        ),
        migrations.AddField(
            model_name='blog',
            name='added_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='body',
            field=models.TextField(default='Add Blog content here'),
        ),
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(default='Add Blog title here', max_length=250, unique=True),
        ),
    ]
