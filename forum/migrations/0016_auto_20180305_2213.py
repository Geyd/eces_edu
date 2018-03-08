# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0015_publication_fichier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professeur',
            name='email',
            field=models.EmailField(max_length=255, help_text='Saisir une adresse e-mail correcte', null=True, unique=True, blank=True),
        ),
    ]
