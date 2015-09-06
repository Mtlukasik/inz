# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ele', '0010_data'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Data',
        ),
    ]
