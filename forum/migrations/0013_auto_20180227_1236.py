# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0012_auto_20180227_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evenement',
            name='fichier',
            field=models.FileField(blank=True, upload_to='post_image/pdf/%Y/%m/%D/', null=True),
        ),
    ]
