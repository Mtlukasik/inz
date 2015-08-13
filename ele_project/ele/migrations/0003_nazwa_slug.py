# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ele', '0002_nazwa'),
    ]

    operations = [
        migrations.AddField(
            model_name='nazwa',
            name='slug',
            field=models.SlugField(default=12, unique=True),
            preserve_default=False,
        ),
    ]
