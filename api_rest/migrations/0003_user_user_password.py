# Generated by Django 4.2.16 on 2024-11-07 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api_rest", "0002_usertasks"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="user_password",
            field=models.CharField(default="", max_length=100),
        ),
    ]
