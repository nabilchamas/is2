# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sprint', '0007_remove_sprint_userstory'),
        ('userstory', '0002_userstory_flujo'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstory',
            name='sprint',
            field=models.ForeignKey(to='sprint.Sprint', null=True),
            preserve_default=True,
        ),
    ]
