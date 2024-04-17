# Generated by Django 5.0.3 on 2024-04-17 05:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("automation", "0002_dataset_user_preprocessing"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="AlgorithmSelection",
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
                ("Linear_Regression", models.BooleanField(default=False)),
                ("Logistic_Regression", models.BooleanField(default=False)),
                ("Decision_Tree", models.BooleanField(default=False)),
                ("Random_Forest", models.BooleanField(default=False)),
                ("Support_Vector_Machines", models.BooleanField(default=False)),
                ("Naive_Bayes", models.BooleanField(default=False)),
                (
                    "dataset",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="automation.dataset",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
