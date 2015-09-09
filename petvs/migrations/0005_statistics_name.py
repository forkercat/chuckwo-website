# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petvs', '0004_statistics_visits'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistics',
            name='name',
            field=models.CharField(default=b'chuck', max_length=200),
        ),
    ]
