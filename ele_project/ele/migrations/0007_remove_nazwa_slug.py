# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ele', '0006_auto_20150813_1327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nazwa',
            name='slug',
        ),
    ]
