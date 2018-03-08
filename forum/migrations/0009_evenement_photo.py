# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0008_auto_20180221_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='evenement',
            name='photo',
            field=models.FileField(upload_to='post_image', blank=True),
        ),
    ]
