# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20180218_1842'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='option',
            options={'ordering': ['option']},
        ),
    ]
