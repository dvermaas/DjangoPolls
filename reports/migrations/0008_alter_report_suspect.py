# Generated by Django 5.0.6 on 2024-05-10 23:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0004_profile_charges"),
        ("reports", "0007_report_suspect"),
    ]

    operations = [
        migrations.AlterField(
            model_name="report",
            name="suspect",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="profiles.profile"
            ),
        ),
    ]
