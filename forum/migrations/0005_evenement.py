# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_auto_20180218_1916'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evenement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('theme', models.CharField(verbose_name='Thème', max_length=200)),
                ('date_eve', models.TextField(verbose_name='Date')),
            ],
            options={
                'ordering': ['-date_eve', 'theme'],
                'get_latest_by': 'date_eve',
            },
        ),
    ]
