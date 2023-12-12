# Generated by Django 4.2 on 2023-11-27 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("module1", "0039_alter_teacherwiseattendence_semester"),
    ]

    operations = [
        migrations.CreateModel(
            name="Address",
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
                ("country", models.CharField(max_length=100)),
                ("state", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=100)),
                ("pin", models.CharField(max_length=20)),
                ("line1", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="ParentDetails",
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
                ("relation", models.CharField(max_length=20)),
                ("name", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=20)),
                ("mail", models.EmailField(max_length=254)),
                ("occupation", models.CharField(max_length=100)),
                ("incomeperannum", models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name="student",
            name="address",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="module1.address",
            ),
        ),
        migrations.AddField(
            model_name="student",
            name="parents",
            field=models.ManyToManyField(to="module1.parentdetails"),
        ),
        migrations.AddField(
            model_name="teacher",
            name="address",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="module1.address",
            ),
        ),
    ]