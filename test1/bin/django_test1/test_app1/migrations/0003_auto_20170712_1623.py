# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app1', '0002_auto_20170712_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logdelete',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
