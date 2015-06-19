# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userstory', '0008_auto_20150618_2344'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userstory',
            old_name='picture',
            new_name='adjunto',
        ),
    ]
