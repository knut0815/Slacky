# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-10-09 00:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hashtags', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hashtag',
            name='tag',
            field=models.CharField(max_length=120),
        ),
    ]
