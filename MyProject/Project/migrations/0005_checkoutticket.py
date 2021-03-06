# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-23 14:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0004_auto_20170922_2354'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckoutTicket',
            fields=[
                ('Receipt_no', models.AutoField(primary_key=True, serialize=False)),
                ('DateTime_out', models.DateTimeField(auto_now_add=True)),
                ('Amount_to_be_paid', models.IntegerField()),
                ('User_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Project.Account')),
            ],
        ),
    ]
