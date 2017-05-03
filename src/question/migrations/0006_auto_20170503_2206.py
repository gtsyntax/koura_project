# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0005_auto_20170503_2148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='questions',
            new_name='question',
        ),
        migrations.AddField(
            model_name='answer',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
