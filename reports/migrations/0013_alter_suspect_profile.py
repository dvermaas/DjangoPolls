# Generated by Django 5.0.7 on 2024-08-03 22:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0004_historicalprofile"),
        ("reports", "0012_legislation_fine_legislation_time_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="suspect",
            name="profile",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="report_appearances",
                to="profiles.profile",
            ),
        ),
    ]
