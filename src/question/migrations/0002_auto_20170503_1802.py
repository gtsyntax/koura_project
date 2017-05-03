# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='active',
        ),
        migrations.RemoveField(
            model_name='question',
            name='draft',
        ),
        migrations.AddField(
            model_name='question',
            name='status',
            field=models.CharField(default=b'draft', max_length=10, choices=[(b'draft', b'DRAFT'), (b'published', b'PUBLISHED')]),
        ),
    ]
