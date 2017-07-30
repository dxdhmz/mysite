# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 01:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0003_auto_20170729_2156'),
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.PositiveIntegerField(max_length=2)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'female')], max_length=2)),
            ],
        ),
    ]
