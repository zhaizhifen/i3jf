# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-21 08:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authx', '0002_customermodel_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='customermodel',
            name='ipohe',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
