# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userstory', '0007_userstory_adjunto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userstory',
            old_name='adjunto',
            new_name='picture',
        ),
    ]
