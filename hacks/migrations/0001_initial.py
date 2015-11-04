# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CodeMania',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(default=None, max_length=254)),
                ('year', models.PositiveIntegerField(default=1)),
                ('phone_number', models.PositiveIntegerField()),
                ('branch', models.CharField(default=b'CSE', max_length=5, choices=[(b'CSE', b'Computer Science and Engineering'), (b'IT', b'Information Technology'), (b'EE', b'Electrical Engineering'), (b'ECE', b'Electronics and Communication Engineering'), (b'EEE', b'Electrical and Electronics Engineering'), (b'CE', b'Civil Engineering'), (b'IC', b'Instrumentation and Control Engineering'), (b'ME', b'Mechanical Engineering'), (b'MT', b'Manufacturing Technology')])),
            ],
        ),
        migrations.CreateModel(
            name='Hackathon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(default=None, max_length=254)),
                ('github', models.CharField(default=None, max_length=200)),
                ('linkedin', models.CharField(default=None, max_length=200)),
                ('size', models.CharField(default=b'L', max_length=5, choices=[(b'S', b'S'), (b'M', b'M'), (b'L', b'L'), (b'XL', b'XL'), (b'XXL', b'XXL')])),
                ('phone_number', models.PositiveIntegerField()),
            ],
        ),
    ]
