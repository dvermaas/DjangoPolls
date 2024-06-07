# Generated by Django 5.0.3 on 2024-03-17 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reports", "0002_tag"),
    ]

    operations = [
        migrations.CreateModel(
            name="Evidence",
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
                ("picture", models.ImageField(upload_to="reports/images")),
            ],
        ),
        migrations.AddField(
            model_name="report",
            name="tags",
            field=models.ManyToManyField(to="reports.tag"),
        ),
    ]