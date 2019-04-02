# Generated by Django 2.1.7 on 2019-04-02 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("testresults", "0012_auto_20190402_0424")]

    operations = [
        migrations.AddIndex(
            model_name="testresultperfsummary",
            index=models.Index(
                fields=["repo", "branch", "flow", "plan", "method", "day"],
                name="lookup",
            ),
        )
    ]
