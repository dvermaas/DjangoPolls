# Generated by Django 5.1.2 on 2024-10-20 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0004_rank_icon"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rank",
            name="icon",
            field=models.FileField(blank=True, null=True, upload_to="accounts/rank"),
        ),
    ]
