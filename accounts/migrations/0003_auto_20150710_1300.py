# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_privatemessage_has_been_read'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='privatemessage',
            options={'ordering': ['-date_created']},
        ),
    ]
