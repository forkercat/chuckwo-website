# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petvs', '0002_pet_hot'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clicks', models.IntegerField(default=0)),
            ],
        ),
    ]
