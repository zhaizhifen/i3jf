# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-25 06:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20170824_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='channelmodel',
            name='categtoy',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Category1Model'),
        ),
    ]