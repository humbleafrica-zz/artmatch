# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-17 09:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0008_auto_20190417_0921'),
    ]

    operations = [
        migrations.RenameField(
            model_name='work',
            old_name='craft',
            new_name='craftid',
        ),
    ]