# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sprint', '0004_auto_20150418_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sprint',
            name='fecha_fin',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
