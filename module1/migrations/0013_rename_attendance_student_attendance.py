# Generated by Django 4.2 on 2023-10-30 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0012_rename_semester_student_semester'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='Attendance',
            new_name='attendance',
        ),
    ]
