# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 19:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('secrets_app', '0004_auto_20170322_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='secret',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secret_likes', to='secrets_app.Secret'),
        ),
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_likes', to='secrets_app.User'),
        ),
        migrations.AlterField(
            model_name='secret',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secrets', to='secrets_app.User'),
        ),
    ]