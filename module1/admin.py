from django.contrib import admin
from .models import *

admin.site.register(Department)
admin.site.register(Semester_Count)
admin.site.register(Subject)
class semester_list(admin.ModelAdmin):
    list_display = ["department","semester_count"]
admin.site.register(Semester,semester_list)
admin.site.register(SemesterWiseSubject)
admin.site.register(SemesterRoutine)
class swsatt(admin.ModelAdmin):
    list_display = ["date","is_present"]
admin.site.register(DailyAttendence,swsatt)
class TWA(admin.ModelAdmin):
    list_display = ["teacher","total_count"]
admin.site.register(TeacherWiseAttendence,TWA)
class attendence(admin.ModelAdmin):
    list_display = ["student"]   
admin.site.register(Attendence,attendence)
class esmlist(admin.ModelAdmin):
    list_display = ["student","exam_name","subject_name","number"]
admin.site.register(EachSubjectMarks,esmlist)
class camlist(admin.ModelAdmin):
    list_display = ["student","exam_name"]
admin.site.register(CAMarks,camlist)
admin.site.register(Marks)
admin.site.register(Address)
admin.site.register(ParentDetails)
class student_list(admin.ModelAdmin):
    list_display = ['name','department']
admin.site.register(Student,student_list)
admin.site.register(Teacher)
admin.site.register(Head_of_Department)
admin.site.register(RoutineCell)
admin.site.register(DailyRoutine)
admin.site.register(TeacherSemesterSubject)
























# from django.contrib import admin
# from .models import *

# admin.site.register(Department)
# admin.site.register(Semester_Count)
# admin.site.register(Subject)

# class semester_list(admin.ModelAdmin):
#     list_display = ["department","semester_count"]
# admin.site.register(Semester,semester_list)

# # class semester_wise_subject(admin.ModelAdmin):
# #     list_display = ["subject","semester"]
# admin.site.register(SemesterWiseSubject)

# admin.site.register(SemesterRoutine)
# class swsatt(admin.ModelAdmin):
#     list_display = ["date","is_present"]
# admin.site.register(DailyAttendence,swsatt)


# class TWA(admin.ModelAdmin):
#     list_display = ["teacher","total_count"]
# admin.site.register(TeacherWiseAttendence,TWA)



# class attendence(admin.ModelAdmin):
#     list_display = ["student"]
    
# admin.site.register(Attendence,attendence)

# class esmlist(admin.ModelAdmin):
#     list_display = ["student","exam_name","subject_name","number"]
# admin.site.register(EachSubjectMarks,esmlist)
# class camlist(admin.ModelAdmin):
#     list_display = ["student","exam_name"]
# admin.site.register(CAMarks,camlist)

# admin.site.register(Marks)

# class student_list(admin.ModelAdmin):
#     list_display = ['name','department']

# admin.site.register(Student,student_list)
# admin.site.register(Teacher)
# admin.site.register(Head_of_Department)
# admin.site.register(RoutineCell)
# admin.site.register(DailyRoutine)
# admin.site.register(TeacherSemesterSubject)
