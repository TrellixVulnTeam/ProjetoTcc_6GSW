# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-20 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Avaliacao', '0011_auto_20170420_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist',
            name='nome',
            field=models.CharField(max_length=80),
        ),
    ]