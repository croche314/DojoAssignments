# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 01:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secrets_app', '0002_auto_20170322_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secret',
            name='num_of_likes',
            field=models.IntegerField(blank=True),
        ),
    ]
