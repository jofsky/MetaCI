# Generated by Django 2.2.16 on 2020-12-15 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("release", "0011_auto_20201120_2124"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="release",
            options={
                "get_latest_by": "created",
                "ordering": ["-created"],
                "verbose_name": "release",
                "verbose_name_plural": "releases",
            },
        ),
    ]
