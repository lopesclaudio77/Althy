# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-04 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0021_post_preview_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='video_preview',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
