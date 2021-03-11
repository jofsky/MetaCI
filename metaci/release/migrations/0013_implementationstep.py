# Generated by Django 3.1.6 on 2021-03-10 20:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("plan", "0036_auto_20210310_2014"),
        ("release", "0012_release_ordering"),
    ]

    operations = [
        migrations.CreateModel(
            name="ImplementationStep",
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
                ("start_time", models.DateTimeField(verbose_name="start_time")),
                ("stop_time", models.DateTimeField(verbose_name="stop_time")),
                (
                    "external_id",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="external id",
                    ),
                ),
                (
                    "plan",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="implementation_steps",
                        to="plan.plan",
                    ),
                ),
                (
                    "release",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="implementation_steps",
                        to="release.release",
                    ),
                ),
            ],
            options={
                "ordering": ("start_time",),
                "unique_together": {("release", "plan")},
            },
        ),
    ]
