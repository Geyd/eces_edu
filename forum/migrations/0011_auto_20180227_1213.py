# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0010_auto_20180227_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evenement',
            name='photo',
            field=models.ImageField(blank=True, upload_to='post_image/%Y/%m/%D/', null=True, width_field='largeur', height_field='hauteur'),
        ),
    ]
