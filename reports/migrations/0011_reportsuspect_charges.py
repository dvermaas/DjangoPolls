# Generated by Django 5.0.6 on 2024-06-04 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reports", "0010_reportsuspect_report_suspects"),
    ]

    operations = [
        migrations.AddField(
            model_name="reportsuspect",
            name="charges",
            field=models.ManyToManyField(to="reports.charge"),
        ),
    ]