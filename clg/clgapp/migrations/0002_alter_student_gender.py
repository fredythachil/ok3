# Generated by Django 4.2.5 on 2023-09-28 05:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("clgapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="gender",
            field=models.CharField(
                choices=[("M", "Male"), ("F", "Female"), ("O", "Other")], max_length=1
            ),
        ),
    ]
