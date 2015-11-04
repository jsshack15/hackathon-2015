# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hacks', '0004_auto_20151104_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hackathon',
            name='hardware_required',
            field=models.TextField(null=True, blank=True),
        ),
    ]
