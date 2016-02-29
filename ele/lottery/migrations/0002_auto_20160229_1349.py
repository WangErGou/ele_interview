# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='winingrecord',
            old_name='shanghai',
            new_name='sh_index',
        ),
        migrations.RenameField(
            model_name='winingrecord',
            old_name='shenzheng',
            new_name='sz_index',
        ),
        migrations.RenameField(
            model_name='winingrecord',
            old_name='win_number',
            new_name='wining_number',
        ),
    ]
