# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-19 15:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Avaliacao', '0023_remove_checklist_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checklist',
            name='especialista',
        ),
        migrations.DeleteModel(
            name='Checklist',
        ),
    ]