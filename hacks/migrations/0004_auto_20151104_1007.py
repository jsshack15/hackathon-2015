# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hacks', '0003_auto_20151104_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hackathon',
            name='hardware_required',
            field=models.TextField(default=None, null=True),
        ),
    ]
