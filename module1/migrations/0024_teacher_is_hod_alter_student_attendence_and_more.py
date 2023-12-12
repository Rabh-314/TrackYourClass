# Generated by Django 4.2 on 2023-11-02 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0023_remove_attendence_sem_wise_attendence_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='is_hod',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='attendence',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='module1.attendence'),
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='module1.department'),
        ),
        migrations.AlterField(
            model_name='student',
            name='semester',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='module1.semester'),
        ),
        migrations.CreateModel(
            name='RoutineCell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module1.semesterwisesubject')),
            ],
        ),
        migrations.CreateModel(
            name='DailyRoutine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=20)),
                ('dailyroutine', models.ManyToManyField(to='module1.routinecell')),
            ],
        ),
        migrations.AddField(
            model_name='teacher',
            name='routine',
            field=models.ManyToManyField(blank=True, to='module1.dailyroutine'),
        ),
    ]
