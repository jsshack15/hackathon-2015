# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hacks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hackathon',
            name='hardware_required',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='hackathon',
            name='mac_address',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
