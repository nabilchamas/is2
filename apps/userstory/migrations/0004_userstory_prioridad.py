# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userstory', '0003_userstory_sprint'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstory',
            name='prioridad',
            field=models.CharField(default=b'Baja', max_length=200, choices=[(b'Baja', b'Baja'), (b'Media', b'Media'), (b'Alta', b'Alta')]),
            preserve_default=True,
        ),
    ]
