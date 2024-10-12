# Generated by Django 4.2.10 on 2024-10-08 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="projectTable",
            fields=[
                ("startDate", models.DateField(auto_created=True, auto_now_add=True)),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("projectTopic", models.CharField(max_length=50)),
                ("projectName", models.CharField(max_length=50)),
                ("projectDescription", models.CharField(max_length=500)),
                ("endDate", models.DateField()),
            ],
        ),
    ]
