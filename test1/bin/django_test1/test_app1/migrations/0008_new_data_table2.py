# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app1', '0007_restoress'),
    ]

    operations = [
        migrations.CreateModel(
            name='new_data_table2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('query', models.CharField(max_length=50)),
                ('answer', models.CharField(max_length=50)),
                ('query_count', models.IntegerField()),
                ('userlist', models.CharField(max_length=1000)),
                ('out_count', models.IntegerField()),
                ('good_count', models.IntegerField()),
                ('bad_count', models.IntegerField()),
                ('export_tag', models.IntegerField()),
            ],
        ),
    ]
