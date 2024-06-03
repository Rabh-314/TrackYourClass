from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Department(models.Model):
    department = models.CharField(max_length=100)
    department_code = models.CharField(max_length=30)
    course_duration = models.PositiveIntegerField()
    def __str__(self):
        return f'{self.department}'

class Semester_Count(models.Model):
    semester_count = models.PositiveIntegerField(default=1)
    def __str__(self):
        return f'{self.semester_count}'

class Subject(models.Model):
    subject = models.CharField(max_length=100)
    subject_code = models.CharField(max_length=20)
    def __str__(self):
        return f'{self.subject}'

class Semester(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    semester_count = models.ForeignKey(Semester_Count, on_delete=models.CASCADE)
    duration = models.DateTimeField(default=timezone.now, null=True)
    def __str__(self):
        return f'{self.semester_count} {self.department}'

class SemesterWiseSubject(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    subject = models.ManyToManyField(Subject)
    def __str__(self):
        return f'{self.semester}'


class ParentDetails(models.Model):
    relation = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    mail = models.EmailField()
    occupation = models.CharField(max_length=100)
    incomeperannum = models.CharField(max_length=100)
    
    def __sts__(self):
        return f'{self.relation} {self.name}'
    
class Address(models.Model):
    country = models.CharField(max_length = 100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin = models.CharField(max_length=20)
    line1 = models.TextField()
    
    def __str__(self):
        return f'{self.country}'
    

class Teacher(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    date_of_joining = models.DateTimeField(default=timezone.now)
    mail = models.EmailField()
    phone = models.CharField(max_length=12)
    address = models.OneToOneField(Address,on_delete=models.SET_NULL,null=True)
    role = models.CharField(max_length=20,default="teacher")
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='image/',null = True)
    is_hod = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.name}'


class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    mail = models.EmailField()
    phone = models.CharField(max_length=12)
    address = models.ForeignKey(Address,on_delete=models.SET_NULL,null=True)
    parents = models.ManyToManyField(ParentDetails)
    role = models.CharField(max_length=20,default="student")
    is_active = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='image/',null = True)
    department = models.ForeignKey(Department,on_delete=models.SET_NULL,null=True)
    semester = models.ForeignKey(Semester,on_delete=models.SET_NULL,null=True)
    
    def __str__(self):
        return self.name
#-------Attendance------------------>>>>>>>>>>>>>>>>>>>>>>

class DailyAttendence(models.Model):
    date = models.DateField(default=timezone.now)
    is_present = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.date}  {self.is_present}'

class TeacherWiseAttendence(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE,null=True)
    dailyattendence = models.ManyToManyField(DailyAttendence)
    total_count = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f'{self.teacher}'


class Attendence(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    teacherwiseattendence = models.ManyToManyField(TeacherWiseAttendence)
    def __str__(self):
        return f'{self.student}'


class Head_of_Department(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return f'{self.teacher}'



#-------Routine----------------->>>>>>>>>>>>>>>>>>>>>>
class TeacherSemesterSubject(models.Model):
    semester = models.ForeignKey(Semester,on_delete=models.CASCADE,null=True)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,null=True)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    subject_code = models.CharField(max_length=20)
    def __str__(self):
        return f'{self.subject_code}'
    
class RoutineCell(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    subject = models.ForeignKey(TeacherSemesterSubject, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.subject} - {self.start_time} to {self.end_time}'

class DailyRoutine(models.Model):
    routine_cell = models.ManyToManyField(RoutineCell)
    day = models.CharField(max_length=20)
    def __str__(self):
        return f'{self.day}'

class SemesterRoutine(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE,null=True)
    daily_routine = models.ManyToManyField(DailyRoutine)
    def __str__(self):
        return f'{self.semester}'


#-------EEEEEEXXXXXXAAAAAAAMMMMMMMMM------------------>>>>>>>>>>>>>>>>>>>>>>
class EachSubjectMarks(models.Model):
    subject_name = models.ForeignKey(TeacherSemesterSubject, on_delete=models.CASCADE,null=True)
    number = models.PositiveIntegerField()
    exam_name = models.CharField(max_length=20,null=True)
    student = models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return f'{self.subject_name}'

class CAMarks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE,null=True)
    exam_name = models.CharField(max_length=20,null=True)
    each_subject_marks = models.ManyToManyField(EachSubjectMarks)
    def __str__(self):
        return f'{self.exam_name}'

class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE,null=True)
    ca_exam = models.ManyToManyField(CAMarks)
    def __str__(self):
        return f'Marks for {self.student}'
