# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0011_auto_20170506_0210'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='height_field',
            field=models.IntegerField(default=250),
        ),
        migrations.AddField(
            model_name='question',
            name='width_field',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(height_field=b'height_field', width_field=b'width_field', null=True, upload_to=b'post_images/', blank=True),
        ),
    ]
