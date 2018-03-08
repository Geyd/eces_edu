# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('matricule', models.CharField(max_length=30, unique=True)),
                ('nom', models.CharField(max_length=120)),
                ('prenom', models.CharField(max_length=150)),
                ('annee', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['nom'],
            },
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('matiere', models.CharField(verbose_name='Matière', max_length=200, unique=True)),
            ],
            options={
                'ordering': ['matiere'],
            },
        ),
        migrations.CreateModel(
            name='Niveau',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('niveau', models.CharField(verbose_name='Niveau', max_length=10, unique=True)),
            ],
            options={
                'ordering': ['niveau'],
            },
        ),
        migrations.CreateModel(
            name='Professeur',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('email', models.EmailField(max_length=255, unique=True, help_text='Saisir une adresse e-mail correcte')),
                ('nom', models.CharField(verbose_name='Nom', max_length=100)),
                ('prenom', models.CharField(verbose_name='Prénom', max_length=150)),
            ],
            options={
                'ordering': ['nom'],
            },
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('titre', models.CharField(max_length=200)),
                ('contenu', models.TextField()),
                ('date_pub', models.DateField(verbose_name='Date Publication', auto_now_add=True)),
                ('professeur', models.ForeignKey(to='forum.Professeur')),
            ],
            options={
                'ordering': ['titre', '-date_pub'],
                'get_latest_by': 'date_pub',
            },
        ),
        migrations.AddField(
            model_name='matiere',
            name='niveau',
            field=models.ForeignKey(to='forum.Niveau'),
        ),
        migrations.AddField(
            model_name='matiere',
            name='professeur',
            field=models.ForeignKey(to='forum.Professeur'),
        ),
        migrations.AddField(
            model_name='etudiant',
            name='niveaux',
            field=models.ManyToManyField(related_name='niveau_etudiant', to='forum.Niveau'),
        ),
    ]
