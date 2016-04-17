# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-17 08:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_name', models.CharField(max_length=10, verbose_name='\u7248\u5757\u540d\u79f0')),
                ('block_desc', models.CharField(max_length=30, verbose_name='\u7248\u5757\u63cf\u8ff0')),
                ('block_admin', models.CharField(max_length=10, verbose_name='\u7ba1\u7406\u5458')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('last_update_timestamp', models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u66f4\u65b0\u65f6\u95f4')),
            ],
        ),
    ]
