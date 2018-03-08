# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_auto_20180218_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evenement',
            name='date_eve',
            field=models.DateField(verbose_name='Date', auto_now_add=True),
        ),
    ]
