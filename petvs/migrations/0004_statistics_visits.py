# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petvs', '0003_statistics'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistics',
            name='visits',
            field=models.IntegerField(default=0),
        ),
    ]
