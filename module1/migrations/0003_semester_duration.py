# Generated by Django 4.2 on 2023-10-28 17:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0002_alter_student_semester_alter_student_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='semester',
            name='duration',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
