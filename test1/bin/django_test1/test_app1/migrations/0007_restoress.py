# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app1', '0006_auto_20170719_2116'),
    ]

    operations = [
        migrations.CreateModel(
            name='restoress',
            fields=[
                ('date', models.DateTimeField()),
                ('user', models.CharField(max_length=50)),
                ('option', models.CharField(max_length=50)),
                ('qaid', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('content', models.CharField(max_length=200)),
                ('query', models.CharField(max_length=50)),
                ('answer', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': '\u6062\u590d\u65e5\u5fd7',
                'verbose_name_plural': '\u6062\u590d\u65e5\u5fd7',
            },
        ),
    ]
