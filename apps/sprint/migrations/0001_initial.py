# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userstory', '0002_userstory_flujo'),
        ('proyecto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateTimeField()),
                ('estado', models.CharField(max_length=15, choices=[(b'No activo', b'No activo'), (b'Activo', b'Activo')])),
                ('descripcion', models.CharField(max_length=200)),
                ('proyecto', models.ForeignKey(to='proyecto.Proyecto')),
                ('userstory', models.ForeignKey(to='userstory.UserStory')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
