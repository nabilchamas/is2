# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userstory', '0006_userstory_desarrollador'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstory',
            name='adjunto',
            field=models.ImageField(null=True, upload_to=b'archivos.Archivo/bytes/filename/mimetype', blank=True),
            preserve_default=True,
        ),
    ]
