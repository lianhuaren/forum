# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-07 09:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usercenter', '0002_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.CharField(blank=True, max_length=300, verbose_name='\u5934\u50cf'),
        ),
    ]
