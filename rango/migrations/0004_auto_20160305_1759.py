# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_auto_20160228_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='likes',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='category',
            name='views',
            field=models.IntegerField(default=10),
        ),
    ]
