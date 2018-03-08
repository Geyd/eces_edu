# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0013_auto_20180227_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evenement',
            name='hauteur',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='evenement',
            name='largeur',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='matiere',
            name='professeur',
            field=models.ForeignKey(to='forum.Professeur'),
        ),
    ]
