# Generated by Django 4.1.5 on 2023-01-21 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("roll_no", models.CharField(max_length=10, unique=True)),
                ("name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=50, unique=True)),
                ("college", models.CharField(max_length=50)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
