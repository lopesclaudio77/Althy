# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-28 10:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_auto_20160427_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.CharField(default=0, max_length=300),
            preserve_default=False,
        ),
    ]
