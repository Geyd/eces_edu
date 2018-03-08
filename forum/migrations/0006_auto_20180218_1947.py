# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_evenement'),
    ]

    operations = [
        migrations.AddField(
            model_name='evenement',
            name='texte',
            field=models.TextField(default=datetime.datetime(2018, 2, 18, 18, 47, 8, 212293, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='evenement',
            name='date_eve',
            field=models.DateField(verbose_name='Date'),
        ),
    ]
