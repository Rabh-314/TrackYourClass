# Generated by Django 4.2 on 2023-10-29 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0003_semester_duration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semester_Count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester_count', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.AlterField(
            model_name='semester',
            name='semester_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
