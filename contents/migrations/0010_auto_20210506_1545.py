# Generated by Django 3.1.7 on 2021-05-06 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0009_auto_20210506_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='menu',
            field=models.OneToOneField(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='contents.menu'),
            preserve_default=False,
        ),
    ]