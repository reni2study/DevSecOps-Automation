# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-03-10 05:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("webscanners", "0006_burp_scan_db_info_vul"),
    ]

    operations = [
        migrations.CreateModel(
            name="status_db",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("status", models.TextField(blank=True, null=True)),
            ],
        ),
    ]