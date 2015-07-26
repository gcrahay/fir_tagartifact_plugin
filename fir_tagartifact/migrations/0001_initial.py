# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0005_auto_20150525_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='ValidTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('description', models.CharField(max_length=100, null=True, verbose_name='Description', blank=True)),
                ('categories', models.ManyToManyField(related_name='valid_tags', verbose_name='Categories', to='incidents.IncidentCategory')),
            ],
            options={
                'verbose_name': 'Valid tag',
                'verbose_name_plural': 'Valid tags',
            },
            bases=(models.Model,),
        ),
    ]
