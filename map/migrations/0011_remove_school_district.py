# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-11 12:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0010_school_district'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='district',
        ),
    ]
