# Generated by Django 4.2.5 on 2023-09-27 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Branch",
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
                ("name", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Department",
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
                ("name", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Purpose",
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
                ("name", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Student",
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
                ("name", models.CharField(max_length=100)),
                ("DOB", models.DateField()),
                ("age", models.IntegerField()),
                ("email", models.EmailField(blank=True, max_length=254)),
                ("phone", models.IntegerField(null=True)),
                ("gender", models.BooleanField(default=False)),
                ("materials", models.BooleanField(blank=True)),
                ("address", models.TextField(blank=True, max_length=50)),
                (
                    "branch",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="clgapp.branch",
                    ),
                ),
                (
                    "department",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="clgapp.department",
                    ),
                ),
                (
                    "purpose",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="clgapp.purpose"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="branch",
            name="department",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="clgapp.department"
            ),
        ),
    ]
