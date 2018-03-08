# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20180218_1846'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='etudiant',
            name='niveaux',
        ),
        migrations.RemoveField(
            model_name='option',
            name='niveaux',
        ),
        migrations.RemoveField(
            model_name='matiere',
            name='niveau',
        ),
        migrations.DeleteModel(
            name='Etudiant',
        ),
        migrations.DeleteModel(
            name='Niveau',
        ),
        migrations.DeleteModel(
            name='Option',
        ),
    ]
