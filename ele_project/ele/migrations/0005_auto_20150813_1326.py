# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ele', '0004_auto_20150813_1318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nazwa',
            name='slug',
        ),
        migrations.AddField(
            model_name='nazwa',
            name='sluga',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
