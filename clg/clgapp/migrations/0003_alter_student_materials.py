# Generated by Django 4.2.5 on 2023-09-28 05:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("clgapp", "0002_alter_student_gender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="materials",
            field=models.CharField(blank=True, max_length=50),
        ),
    ]