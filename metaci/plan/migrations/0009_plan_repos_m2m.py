# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-23 19:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("repository", "0001_initial"), ("plan", "0008_plan_yaml_config")]

    operations = [
        migrations.CreateModel(
            name="PlanRepository",
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
                (
                    "plan",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="plan.Plan"
                    ),
                ),
                (
                    "repo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="repository.Repository",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="plan",
            name="repos",
            field=models.ManyToManyField(
                through="plan.PlanRepository", to="repository.Repository"
            ),
        ),
    ]
