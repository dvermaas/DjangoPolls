# Generated by Django 5.0.6 on 2024-06-21 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="tag",
            name="icon",
            field=models.CharField(default="circle-fill", max_length=32),
        ),
    ]
