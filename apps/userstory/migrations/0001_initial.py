# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flujo', '0004_flujo_proyecto'),
        ('proyecto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserStory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('estado', models.CharField(max_length=200, choices=[(b'Todo', b'To do'), (b'Doing', b'Doing'), (b'Done', b'Done')])),
                ('actividad', models.ForeignKey(to='flujo.Actividad')),
                ('proyecto', models.ForeignKey(to='proyecto.Proyecto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
