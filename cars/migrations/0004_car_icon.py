# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-24 16:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_auto_20180224_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='icon',
            field=models.CharField(default='test.png', max_length=350),
            preserve_default=False,
        ),
    ]
