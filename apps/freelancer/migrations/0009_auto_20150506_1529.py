# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal
import django.core.validators
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('freelancer', '0008_auto_20150420_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freelancer',
            name='minimum_pay_per_hour',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('6.75'), max_digits=5, validators=[django.core.validators.MinValueValidator(Decimal('6.75'))], help_text=b'The minimum pay per hour you will accept.', default_currency=b'GBP'),
            preserve_default=True,
        ),
    ]
