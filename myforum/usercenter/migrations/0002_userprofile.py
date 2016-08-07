# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-07 07:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usercenter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.IntegerField(choices=[(0, '\u7537'), (-1, '\u5973')], default=0, verbose_name='\u6027\u522b')),
                ('birthday', models.DateTimeField(blank=True, null=True, verbose_name='\u751f\u65e5')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]