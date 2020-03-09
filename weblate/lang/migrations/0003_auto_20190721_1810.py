# -*- coding: utf-8 -*-
# Generated by Django 2.2.1 on 2019-07-21 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("lang", "0002_auto_20190516_1245")]

    operations = [
        migrations.AlterField(
            model_name="plural",
            name="source",
            field=models.SmallIntegerField(
                choices=[(0, "Default plural"), (1, "Plural gettext formula")],
                default=0,
                verbose_name="Plural definition source",
            ),
        )
    ]
