# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sprint', '0005_auto_20150418_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sprint',
            name='estado',
            field=models.CharField(max_length=15, choices=[(b'Activo', b'Activo'), (b'No activo', b'No activo')]),
            preserve_default=True,
        ),
    ]
