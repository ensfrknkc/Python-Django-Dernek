# Generated by Django 3.1.7 on 2021-05-01 19:05

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210430_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='aboutus',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='contact',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='references',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]
