# Generated by Django 5.1.2 on 2024-10-19 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_alter_user_badge_number_alter_user_rank"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="badge_number",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]