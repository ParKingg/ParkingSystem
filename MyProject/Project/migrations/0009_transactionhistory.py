# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 07:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0008_reserveparking_paid'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionHistory',
            fields=[
                ('Transact_id', models.AutoField(primary_key=True, serialize=False)),
                ('Time_in', models.TimeField()),
                ('Date_in', models.DateField()),
                ('DateTime_out', models.DateTimeField()),
                ('Total_Cost', models.PositiveIntegerField()),
                ('Slot_no', models.IntegerField()),
                ('Plate_no', models.CharField(max_length=8)),
                ('Payment_Status', models.CharField(max_length=10)),
                ('Receipt_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Project.ReservationFee')),
                ('Reserve_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Project.ReserveParking')),
                ('User_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Project.Account')),
            ],
        ),
    ]
