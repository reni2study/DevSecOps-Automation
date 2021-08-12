# Generated by Django 3.1.12 on 2021-07-19 16:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("projects", "0015_auto_20210719_1431"),
    ]

    operations = [
        migrations.CreateModel(
            name="NmapResultDb",
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
                ("scan_id", models.TextField(blank=True, null=True)),
                ("ip_address", models.TextField(blank=True, null=True)),
                ("protocol", models.TextField(blank=True, null=True)),
                ("port", models.TextField(blank=True, null=True)),
                ("state", models.TextField(blank=True, null=True)),
                ("reason", models.TextField(blank=True, null=True)),
                ("reason_ttl", models.TextField(blank=True, null=True)),
                ("version", models.TextField(blank=True, null=True)),
                ("extrainfo", models.TextField(blank=True, null=True)),
                ("name", models.TextField(blank=True, null=True)),
                ("conf", models.TextField(blank=True, null=True)),
                ("method", models.TextField(blank=True, null=True)),
                ("type_p", models.TextField(blank=True, null=True)),
                ("osfamily", models.TextField(blank=True, null=True)),
                ("vendor", models.TextField(blank=True, null=True)),
                ("osgen", models.TextField(blank=True, null=True)),
                ("accuracy", models.TextField(blank=True, null=True)),
                ("cpe", models.TextField(blank=True, null=True)),
                ("used_state", models.TextField(blank=True, null=True)),
                ("used_portid", models.TextField(blank=True, null=True)),
                ("used_proto", models.TextField(blank=True, null=True)),
                (
                    "project",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="projects.projectdb",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="NmapVulnersPortResultDb",
            fields=[
                (
                    "nmapresultdb_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="tools.nmapresultdb",
                    ),
                ),
                ("vulners_extrainfo", models.TextField(blank=True, null=True)),
            ],
            bases=("tools.nmapresultdb",),
        ),
        migrations.CreateModel(
            name="SslscanResultDb",
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
                ("scan_id", models.TextField(blank=True, null=True)),
                ("scan_url", models.TextField(blank=True, null=True)),
                ("sslscan_output", models.TextField(blank=True, null=True)),
                (
                    "project",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="projects.projectdb",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="NmapScanDb",
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
                ("scan_id", models.TextField(blank=True, null=True)),
                ("scan_ip", models.TextField(blank=True, null=True)),
                ("total_ports", models.TextField(blank=True, null=True)),
                ("total_open_ports", models.TextField(blank=True, null=True)),
                ("total_close_ports", models.TextField(blank=True, null=True)),
                (
                    "project",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="projects.projectdb",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="NiktoVulnDb",
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
                ("vuln_id", models.UUIDField(blank=True, null=True)),
                ("scan_id", models.UUIDField(blank=True, null=True)),
                ("scan_url", models.TextField(blank=True, null=True)),
                ("discription", models.TextField(blank=True, null=True)),
                ("targetip", models.TextField(blank=True, null=True)),
                ("hostname", models.TextField(blank=True, null=True)),
                ("port", models.TextField(blank=True, null=True)),
                ("uri", models.TextField(blank=True, null=True)),
                ("httpmethod", models.TextField(blank=True, null=True)),
                ("testlinks", models.TextField(blank=True, null=True)),
                ("osvdb", models.TextField(blank=True, null=True)),
                ("false_positive", models.TextField(blank=True, null=True)),
                ("jira_ticket", models.TextField(blank=True, null=True)),
                ("vuln_status", models.TextField(blank=True, null=True)),
                ("dup_hash", models.TextField(blank=True, null=True)),
                ("vuln_duplicate", models.TextField(blank=True, null=True)),
                ("false_positive_hash", models.TextField(blank=True, null=True)),
                ("date_time", models.TextField(blank=True, null=True)),
                (
                    "project",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="projects.projectdb",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="NiktoResultDb",
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
                ("scan_id", models.TextField(blank=True, null=True)),
                ("scan_url", models.TextField(blank=True, null=True)),
                ("nikto_scan_output", models.TextField(blank=True, null=True)),
                ("date_time", models.TextField(blank=True, null=True)),
                ("nikto_status", models.TextField(blank=True, null=True)),
                (
                    "project",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="projects.projectdb",
                    ),
                ),
            ],
        ),
    ]