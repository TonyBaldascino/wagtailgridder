# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-07 17:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailgridder', '0011_auto_20170404_1454'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gridindexgriditemrelationship',
            old_name='GridRelationship',
            new_name='grid_relationship',
        ),
    ]