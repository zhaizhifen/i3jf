# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-25 09:21
from __future__ import unicode_literals

from django.db import migrations, models
import utils.misc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20170825_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepagecirclemodel',
            name='backend_image',
            field=models.ImageField(blank=True, null=True, upload_to=utils.misc.GetCategoryImageUpload, verbose_name='\u80cc\u666f\u56fe\u7247'),
        ),
    ]
