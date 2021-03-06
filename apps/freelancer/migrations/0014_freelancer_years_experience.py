# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('freelancer', '0013_auto_20150618_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='freelancer',
            name='years_experience',
            field=models.PositiveSmallIntegerField(default=1, choices=[(0, b'Less than 1 year'), (1, b'1 - 3 years'), (3, b'3 - 5 years'), (5, b'More than 5 years')]),
            preserve_default=True,
        ),
    ]
