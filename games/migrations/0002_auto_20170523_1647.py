# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-23 14:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='consoles',
            field=models.ManyToManyField(blank=True, to='games.Console'),
        ),
    ]
