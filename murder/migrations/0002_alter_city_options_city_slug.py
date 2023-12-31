# Generated by Django 5.0 on 2023-12-29 15:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("murder", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="city",
            options={"verbose_name_plural": "Cities"},
        ),
        migrations.AddField(
            model_name="city",
            name="slug",
            field=models.SlugField(default="ville", max_length=128),
            preserve_default=False,
        ),
    ]
