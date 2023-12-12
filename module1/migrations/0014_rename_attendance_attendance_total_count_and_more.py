# Generated by Django 4.2 on 2023-10-30 18:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0013_rename_attendance_student_attendance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='attendance',
            new_name='total_count',
        ),
        migrations.RemoveField(
            model_name='student',
            name='attendance',
        ),
        migrations.AddField(
            model_name='attendance',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='attendance',
            name='is_present',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='attendance',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='module1.student'),
        ),
    ]
