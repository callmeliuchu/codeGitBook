# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-03 13:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books_recsys_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='arrayratedmoviesindxs',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='name',
        ),
    ]
