# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0014_auto_20180301_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='fichier',
            field=models.FileField(null=True, upload_to='post_image/pdf/%Y/%m/%D/', blank=True),
        ),
    ]
