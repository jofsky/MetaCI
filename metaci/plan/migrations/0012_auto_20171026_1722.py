# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-26 17:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("plan", "0011_remove_plan_repo")]

    operations = [
        migrations.AlterModelOptions(
            name="plan", options={"ordering": ["name", "active", "context"]}
        ),
        migrations.AlterModelOptions(
            name="planrepository", options={"verbose_name_plural": "Plan Repositories"}
        ),
        migrations.AlterModelOptions(
            name="planschedule", options={"verbose_name_plural": "Plan Schedules"}
        ),
        migrations.AlterField(
            model_name="plan",
            name="repos",
            field=models.ManyToManyField(
                related_name="plans",
                through="plan.PlanRepository",
                to="repository.Repository",
            ),
        ),
    ]
