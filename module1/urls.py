from django.urls import path
from .views import *

urlpatterns = [
    path('',Home),
    path('loginpage/',LoginPage),
    path('signinpage/',SigninPage),
    path('logoutpage/',LogoutPage),
    path('adminhomepage/',AdminHomePage),
    path('addnewdepartment/',AddNewDepartment),
    path('departmentlist/',DepartmentList),
    path('addnewteacher/',AddNewTeacher),
    path('addsubject/',AddSubject),
    path('subjectlist/',SubjectList),
    path('teacherlist/',TeacherList),
    path('studentlist/',StudentList),
    path('pendingstudent/',PendingStudent),
    path('accepted/<id>/',Accepted),
    path('notaccepted/<id>/',NotAccepted),
    path('studenthomepage/<id>/',StudentHomePage),
    path('teacherhomepage/<id>/',TeacherHomePage),
    path('hodhomepage/<id>/',HODHomePage),
    path('semdata/',SemData),
    path('addnewsem/',AddNewSem),
    path('addhod/',AddHOD),
    path('teacherforsemester/<id>/<hodid>/',TeacherForSemester),
    path('routine/<id1>/<semid>/',Routine),
    path('marks/<id>/<semid>/',Mark),
    path('teachervisit/<id>/<hodid>/',TeacherVisit),
    path('studentvisit/<id>/<hodid>/',StudentVisit),
    path('studentvisitprofile/<id>/<hodid>/',StudentVisitProfile),
    path('seemarks/<semid>/<hodid>/',SeeMarks),
    path('lockviewmarks/<hodid>/<semid>/',LockViewMarks),
    path('studentdailyattendance/<semid>/<hodid>/',StudentDailyAttendence),
]
