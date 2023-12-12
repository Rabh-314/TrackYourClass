# Generated by Django 4.2 on 2023-10-25 15:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=100)),
                ('department_code', models.CharField(max_length=30)),
                ('course_duration', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester_count', models.IntegerField(default=1)),
                ('attendence', models.PositiveIntegerField(default=0)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module1.department')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('subject_code', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('gender', models.CharField(max_length=10)),
                ('date_of_birth', models.DateField()),
                ('date_of_joining', models.DateTimeField(default=django.utils.timezone.now)),
                ('mail', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=12)),
                ('role', models.CharField(default='teacher', max_length=20)),
                ('photo', models.ImageField(null=True, upload_to='image/')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module1.department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('gender', models.CharField(max_length=10)),
                ('date_of_birth', models.DateField()),
                ('mail', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=12)),
                ('role', models.CharField(default='student', max_length=20)),
                ('is_active', models.BooleanField(default=False)),
                ('photo', models.ImageField(null=True, upload_to='image/')),
                ('Semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module1.semester')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module1.department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SemesterWiseSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module1.semester')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module1.subject')),
            ],
        ),
        migrations.AddField(
            model_name='semester',
            name='sem_wise_sub',
            field=models.ManyToManyField(through='module1.SemesterWiseSubject', to='module1.subject'),
        ),
        migrations.CreateModel(
            name='Head_of_Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module1.teacher')),
            ],
        ),
    ]
