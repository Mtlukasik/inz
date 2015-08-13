# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ele', '0003_nazwa_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nazwa',
            name='slug',
            field=models.SlugField(),
        ),
    ]
