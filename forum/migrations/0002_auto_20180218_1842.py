# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('option', models.CharField(verbose_name='Option', max_length=200, unique=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='niveau',
            options={'verbose_name_plural': 'Niveaux', 'ordering': ['niveau']},
        ),
        migrations.AddField(
            model_name='option',
            name='niveaux',
            field=models.ManyToManyField(verbose_name='Niveau', related_name='option_niveau', to='forum.Niveau'),
        ),
    ]
