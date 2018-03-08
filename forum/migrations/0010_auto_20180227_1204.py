# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0009_evenement_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='evenement',
            name='fichier',
            field=models.FileField(blank=True, upload_to='pdf/%Y/%m/%D/', null=True),
        ),
        migrations.AlterField(
            model_name='evenement',
            name='photo',
            field=models.ImageField(blank=True, upload_to='post_image/%Y/%m/%D/', null=True),
        ),
    ]
