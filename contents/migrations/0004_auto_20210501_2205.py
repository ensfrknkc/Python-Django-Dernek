# Generated by Django 3.1.7 on 2021-05-01 19:05

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0003_auto_20210430_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='detail',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]