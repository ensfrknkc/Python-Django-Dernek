# Generated by Django 3.1.7 on 2021-05-10 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0015_auto_20210506_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
