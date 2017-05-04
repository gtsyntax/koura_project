# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0008_auto_20170504_1802'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='status',
        ),
    ]
