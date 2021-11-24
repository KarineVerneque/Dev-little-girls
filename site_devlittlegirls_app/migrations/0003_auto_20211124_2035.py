# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_devlittlegirls_app', '0002_auto_20211124_1949'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='site_devlittlegirls',
            new_name='Site',
        ),
    ]
