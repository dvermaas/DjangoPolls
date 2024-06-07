# Generated by Django 5.0.3 on 2024-05-09 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reports", "0005_report_is_plead_guilty_report_is_processed_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Charge",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=256)),
                ("description", models.TextField(max_length=1024)),
            ],
        ),
    ]