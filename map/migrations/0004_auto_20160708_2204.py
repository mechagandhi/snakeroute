# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-08 22:04
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0003_auto_20160708_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schooldistrict',
            name='geom',
            field=django.contrib.gis.db.models.fields.PolygonField(srid=-1),
        ),
    ]
