# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0011_auto_20180227_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='evenement',
            name='hauteur',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='evenement',
            name='largeur',
            field=models.IntegerField(default=0),
        ),
    ]
