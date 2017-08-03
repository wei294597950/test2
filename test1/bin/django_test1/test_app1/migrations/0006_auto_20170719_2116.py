# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app1', '0005_restore'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restore',
            name='content',
            field=models.CharField(max_length=200),
        ),
    ]
