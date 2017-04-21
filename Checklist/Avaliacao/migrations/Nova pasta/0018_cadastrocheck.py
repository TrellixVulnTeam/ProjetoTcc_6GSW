# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-19 14:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0005_auto_20170320_1451'),
        ('Avaliacao', '0017_auto_20170419_1138'),
    ]

    operations = [
        migrations.CreateModel(
            name='CadastroCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('desc', models.CharField(max_length=255, null=True)),
                ('categoria', models.ManyToManyField(to='Avaliacao.Categoria')),
                ('elaborador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuario.Usuario')),
            ],
        ),
    ]