# Generated by Django 3.1.7 on 2021-05-06 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0013_auto_20210506_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
