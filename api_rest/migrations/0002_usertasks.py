# Generated by Django 4.2.16 on 2024-11-07 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api_rest", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserTasks",
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
                ("task_name", models.CharField(default="", max_length=100)),
                ("task_description", models.CharField(default="", max_length=100)),
                ("task_status", models.BooleanField(default=False)),
                (
                    "user_nickname",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api_rest.user"
                    ),
                ),
            ],
            options={
                "verbose_name": "User Task",
                "verbose_name_plural": "User Tasks",
                "db_table": "user_tasks",
            },
        ),
    ]
