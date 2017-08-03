# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='logdelete',
            fields=[
                ('date', models.DateTimeField()),
                ('cluster', models.CharField(max_length=50)),
                ('index', models.CharField(max_length=50)),
                ('types', models.CharField(max_length=50)),
                ('qaid', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('query', models.CharField(max_length=50)),
                ('answer', models.CharField(max_length=50)),
            ],
        ),
    ]
