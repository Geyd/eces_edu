# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0007_auto_20180221_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matiere',
            name='professeur',
            field=models.ForeignKey(related_name='matiere_professeur', to='forum.Professeur'),
        ),
    ]
