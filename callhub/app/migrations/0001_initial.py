# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fibonacci',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('index', models.BigIntegerField(default=None)),
                ('result', models.BigIntegerField(default=None)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
