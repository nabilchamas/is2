# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userstory', '0004_userstory_prioridad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstory',
            name='prioridad',
            field=models.CharField(max_length=200, null=True, choices=[(b'Baja', b'Baja'), (b'Media', b'Media'), (b'Alta', b'Alta')]),
            preserve_default=True,
        ),
    ]
