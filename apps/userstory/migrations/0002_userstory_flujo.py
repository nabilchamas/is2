# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flujo', '0004_flujo_proyecto'),
        ('userstory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstory',
            name='flujo',
            field=models.ForeignKey(to='flujo.Flujo', null=True),
            preserve_default=True,
        ),
    ]
