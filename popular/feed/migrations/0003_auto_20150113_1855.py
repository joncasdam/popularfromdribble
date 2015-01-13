# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_entrada'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entrada',
            old_name='dirbble_id',
            new_name='dribble_id',
        ),
    ]
