# Generated by Django 5.0.6 on 2024-06-12 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0001_initial"),
        ("reports", "0006_alter_suspect_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="report",
            name="tags",
            field=models.ManyToManyField(blank=True, to="common.tag"),
        ),
    ]
