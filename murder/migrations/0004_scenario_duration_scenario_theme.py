# Generated by Django 5.0 on 2023-12-29 16:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("murder", "0003_scenario_slug_alter_scenario_picture_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="scenario",
            name="duration",
            field=models.IntegerField(default=60, help_text="In minutes"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="scenario",
            name="theme",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="murder.theme",
            ),
            preserve_default=False,
        ),
    ]
