# Generated by Django 4.2 on 2023-11-25 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0038_remove_attendence_semester_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherwiseattendence',
            name='semester',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='module1.semester'),
        ),
    ]
