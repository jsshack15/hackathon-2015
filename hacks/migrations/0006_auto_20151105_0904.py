# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hacks', '0005_auto_20151104_1040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='codemania',
            name='id',
        ),
        migrations.RemoveField(
            model_name='hackathon',
            name='id',
        ),
        migrations.AddField(
            model_name='codemania',
            name='course',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='codemania',
            name='branch',
            field=models.CharField(max_length=5, null=True, choices=[(b'CSE', b'Computer Science and Engineering'), (b'IT', b'Information Technology'), (b'EE', b'Electrical Engineering'), (b'ECE', b'Electronics and Communication Engineering'), (b'EEE', b'Electrical and Electronics Engineering'), (b'CE', b'Civil Engineering'), (b'IC', b'Instrumentation and Control Engineering'), (b'ME', b'Mechanical Engineering'), (b'MT', b'Manufacturing Technology')]),
        ),
        migrations.AlterField(
            model_name='codemania',
            name='email',
            field=models.EmailField(default=None, max_length=254, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='codemania',
            name='year',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='hackathon',
            name='email',
            field=models.EmailField(default=None, max_length=254, serialize=False, primary_key=True),
        ),
    ]
