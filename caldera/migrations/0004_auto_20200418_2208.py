# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-04-18 15:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caldera', '0003_auto_20200214_1055'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='spesial',
            index_together=set([]),
        ),
        migrations.RemoveField(
            model_name='spesial',
            name='category',
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',)},
        ),
        migrations.DeleteModel(
            name='Spesial',
        ),
    ]
