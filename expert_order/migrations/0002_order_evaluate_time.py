# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-04-19 10:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expert_order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='evaluate_time',
            field=models.DateTimeField(null=True),
        ),
    ]
