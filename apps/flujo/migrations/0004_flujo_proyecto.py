# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0001_initial'),
        ('flujo', '0003_remove_flujo_proyecto'),
    ]

    operations = [
        migrations.AddField(
            model_name='flujo',
            name='proyecto',
            field=models.ForeignKey(to='proyecto.Proyecto', null=True),
            preserve_default=True,
        ),
    ]
