from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import *
import json
from datetime import *
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
import random



def Home(request):
    return render(request, "home.html")

def SigninPage(request):
    dept = Department.objects.all()
    try:
        if request.method == 'POST':
            data = request.POST
            # Student Details
            studentfirstname = data.get("fname")
            studentlastname = data.get("lname")
            studentdob = data.get("dob")
            studentgender = data.get("gender")
            studentphone = data.get("phone")
            studentmail = data.get("mail")
            studentphoto = request.FILES.get("photo")
            studentdept = data.get("dept")
            name = studentfirstname+" "+studentlastname
            userName = name.replace(" ","")
            sdept = Department.objects.get(id = studentdept)
            # Mothers Details
            motherfname = data.get("Mfname")
            motherlname = data.get("Mlname")
            motherphone = data.get("Mphone")
            mothermalil = data.get("Mmail")
            motheroccupassion = data.get("Moccupassion")
            motherincome = data.get("Mincome")
            Mname = motherfname+" "+motherlname
            # Fathers Details
            fatherfname = data.get("Ffname")
            fatherlname = data.get("Flname")
            fatherphone = data.get("Fphone")
            fathermalil = data.get("Fmail")
            fatheroccupassion = data.get("Foccupassion")
            fatherincome = data.get("Fincome")
            Fname = fatherfname+" "+fatherlname
            # Address
            state = data.get("state")
            city = data.get("city")
            country = data.get("country")
            pin = data.get("pin")
            line1 = data.get("line1")
            mother = ParentDetails.objects.create(
                relation = "Mother",
                name = Mname,
                phone = motherphone,
                mail = mothermalil,
                occupation = motheroccupassion,
                incomeperannum = motherincome
            )
            mother.save()
            father = ParentDetails.objects.create(
                relation = "Father",
                name = Fname,
                phone = fatherphone,
                mail = fathermalil,
                occupation = fatheroccupassion,
                incomeperannum = fatherincome
            )
            father.save()
            user = User.objects.create(
                username = userName
            )
            user.set_password(userName)
            user.save()
            address = Address.objects.create(
                country = country,
                city = city,
                state = state,
                pin = pin,
                line1 = line1
            )
            address.save()
            student = Student.objects.create(
                user = user,
                name = name,
                gender = studentgender,
                date_of_birth = studentdob,
                mail = studentmail,
                phone = studentphone,
                address = address,
                photo = studentphoto,
                department = sdept
            )
            student.parents.add(mother,father)
            student.save()
    except Exception as e:
        messages.error(request,"Something Went Wrong")   
    return render(request,'SigninPage.html',{'context':dept})



def LoginPage(request):
    if request.method == "POST":
        data = request.POST
        uname = data.get("username")
        pword = data.get("password")
        if not (User.objects.filter(username=uname).exists()):
            messages.error(request, "Username do not exist")
            return redirect("/loginpage/")
        else:
            check = authenticate(username=uname, password=pword)

            if check is not None:
                login(request, check)
                temp = User.objects.get(username=uname)

                if temp.is_superuser:
                    return redirect("/adminhomepage/")
                if Teacher.objects.filter(user=temp).exists():
                    hold = Teacher.objects.filter(user=temp)[0]
                else:
                    hold = Student.objects.filter(user=temp)[0]

                if hold.role == "student":
                    if hold.is_active == True:
                        id = hold.id

                        return redirect(f"/studenthomepage/{id}/")
                    else:
                        return HttpResponse("Not Yet Verified")
                elif hold.role == "teacher":
                    id = hold.id
                    if hold.is_hod == True:
                        return redirect(f"/hodhomepage/{id}/")
                    else:
                        # return redirect(f'/teacherhomepage/{id}/')
                        return redirect(f"/hodhomepage/{id}/")

            else:
                messages.error(request, "Invalid Password")
                return redirect("/loginpage/")
    return render(request, "LoginPage.html")


def LogoutPage(request):
    logout(request)
    return redirect("/loginpage/")


@login_required
def TeacherHomePage(request, id):
    teacher = Teacher.objects.filter(id=id)
    hold = teacher[0]
    dept = hold.department
    dept_temp = Department.objects.get(department=dept)
    semester = Semester.objects.filter(department=dept_temp)
    student = Student.objects.filter(department=dept_temp)
    filtered_list = TeacherSemesterSubject.objects.filter(teacher=hold)
    return render(
        request,
        "TeacherHomePage.html",
        {
            "context": teacher,
            "student": student,
            "id": id,
            "semester": semester,
            "filtered_list": filtered_list,
        },
    )


@login_required
def AdminHomePage(request):
    student = Student.objects.all()
    teacher = Teacher.objects.all()
    teacher_length = len(teacher)
    student_length = len(student)
    return render(request, "AdminHomePage.html",{'teacher_length':teacher_length,'student_length':student_length})


@login_required
def AddNewDepartment(request):
    try:
        if request.method == "POST":
            data = request.POST
            dept_name = data.get("deptname").upper()
            dept_code = data.get("deptcode")
            duration = int(data.get("duration"))
            if Department.objects.filter(department=dept_name).exists():
                messages.error(request, "Department already exists")
                return redirect("/addnewdepartment/")
            else:
                Department.objects.create(
                    department=dept_name,
                    department_code=dept_code,
                    course_duration=duration,
                )
                messages.success(request,"Successfully added")
    except:
        messages.error(request, "some error occured")
        return redirect("/addnewdepartment/")
    return render(request, "AddNewDepartment.html")


@login_required
def DepartmentList(request):
    dept = Department.objects.all()
    return render(request, "DepartmentList.html", {"context": dept})


@login_required
def AddNewTeacher(request):
    try:
        dept = Department.objects.all()
        if request.method == "POST":
            data = request.POST
            name = data.get("name")
            dob = data.get("dob")
            gender = data.get("gender")
            mail = data.get("mail")
            phone = data.get("phone")
            dept_code = data.get("dept")
            photo = request.FILES.get("photo")
            pword = name.replace(" ", "").lower()
            uname = pword + str(random.randint(0,999))
            department = Department.objects.get(department_code=dept_code)

            if User.objects.filter(username=uname).exists():
                messages.error(request, "Username exist")
            user = User.objects.create(username=uname)
            user.set_password(pword)
            user.save()
            Teacher.objects.create(
                user=user,
                name=name,
                gender=gender,
                date_of_birth=dob,
                mail=mail,
                phone=phone,
                photo=photo,
                department=department,
            )
            messages.success(request,"Teacher added succesfully")
    except Exception as e:
        messages.error(request,f"An unexpected error occured {e}")
    return render(request, "AddNewTeacher.html", {"context": dept})


@login_required
def AddSubject(request):
    error_this =""
    try:
        if request.method == "POST":
            data = request.POST
            sub_name = data.get("subname")
            sub_code = data.get("subcode")
            if Subject.objects.filter(subject=sub_name).exists():
                messages.error(request, "Subject already exists")
            else:
                Subject.objects.create(
                    subject=sub_name,
                    subject_code=sub_code,
                )
                messages.success(request,"Succesfully added")
    except:
        error_this = "An unexpected error occured ,Please insert data carefully"
    return render(request, "AddSubject.html",{'error_this':error_this})


@login_required
def SubjectList(request):
    subject = Subject.objects.all()
    return render(request, "SubjectList.html", {"context": subject})


@login_required
def TeacherList(request):
    dept = Department.objects.all()
    try:
        if request.method == 'POST':
            dept_filter = int(request.POST.get('dept'))
            teacher = Teacher.objects.filter(department__id = dept_filter)
            return render(request, "TeacherList.html", {"dept": dept,'context':teacher})
    except Exception as e:
        messages.error(request,f'something went wrong::{e}')
    return render(request, "TeacherList.html", {"dept": dept})


@login_required
def StudentList(request):
    dept = Department.objects.all()
    
    if request.method == 'POST':
        try:
            dept_filter = int(request.POST.get('dept'))
            student = Student.objects.filter(is_active=True,department__id = dept_filter)
            return render(request, "StudentList.html", {"dept": dept,'context':student})
        except Exception as e:
            messages.error(request,f'something went wrong::{e}')
    return render(request, "StudentList.html", {"dept": dept})


@login_required
def PendingStudent(request):
    student = Student.objects.filter(is_active=False)
    length = len(student)
    
    return render(request, "PendingStudent.html", {"context": student,'length':length})


@login_required
def Accepted(request, id):
    p = Student.objects.get(id=id)
    p.is_active = True
    p.save()
    return redirect("/pendingstudent/")


@login_required
def NotAccepted(request, id):
    Student.objects.get(id=id).delete()
    return redirect("/pendingstudent/")


@login_required
def SemData(request):
    return render(request, "SemData.html")


@login_required
def AddNewSem(request):
    try:
        dept = Department.objects.all()
        sem = Semester_Count.objects.all()
        sub_all = Subject.objects.all()
        sub_list = ["sub1", "sub2", "sub3", "sub4", "sub5"]
        error_this = ""
        if request.method == "POST":
            data = request.POST
            department = data.get("dept")
            semester = data.get("sem")
            d = Department.objects.get(department=department)
            s = Semester_Count.objects.get(semester_count=semester)
            try:
                p = Semester.objects.get(semester_count=s)
            except:
                p = Semester.objects.create(department=d, semester_count=s)
                p.save()
            semwisesub = SemesterWiseSubject.objects.create(semester=p)
            for i in sub_list:
                sub = data.get(f"{i}")
            
                try:
                    subject = Subject.objects.get(id = int(sub))
                except ObjectDoesNotExist:
                    error_this = f"Subject '{sub}' does not exist."
                semwisesub.subject.add(subject)
            semwisesub.save()
            messages.success(request,"New semester data added")
    except Exception as e:
        error_this = f'an unexpected error occured please insert data carefully'
    return render(
        request,
        "AddNewSem.html",
        {
            "dept": dept,
            "sem": sem,
            "sub": sub_all,
            "sub_list": sub_list,
            "error_this": error_this,
        },
    )


@login_required
def AddHOD(request):
    dept = Department.objects.all()
    teacher = Teacher.objects.all()
    error_this = ""
    if request.method == 'POST':
        data = request.POST
        dept_id = int(data.get('dept'))
        teacher_id = int(data.get('teacher'))
        try:
            dept_temp = Department.objects.get(id = dept_id)
            teacher_temp = Teacher.objects.get(id = teacher_id)
            try:
                current_hod = Head_of_Department.objects.get(department = dept_temp).teacher
                current_hod.is_hod =False
                Head_of_Department.objects.get(department = dept_temp).delete()
            except:    
                Head_of_Department.objects.create(
                    department = dept_temp,
                    teacher = teacher_temp
                )
            teacher_temp.is_hod = True
            teacher_temp.save()
            messages.success(request,"HOD updated succesfully")
            
        except Exception as e:
            error_this = f"an unexpected error has occured {e}"
            
    return render(request, "AddHOD.html", {"dept": dept, "teacher": teacher,'error_this':error_this})


def fetch_me_the_data(id):
    try:
        hold = Teacher.objects.get(id=id)
    except Teacher.DoesNotExist:
        raise ValueError(f"No teacher found with ID {id}")
    dept_temp = hold.department
    semester = Semester.objects.filter(department=dept_temp)
    student = Student.objects.filter(department=dept_temp)
    teachers_under = Teacher.objects.filter(department=dept_temp)
    dept = dept_temp.department
    today = datetime.now()
    day_name = today.strftime("%A")
    filtered_list = TeacherSemesterSubject.objects.filter(teacher=hold)
    sem_rout = SemesterRoutine.objects.filter(semester__department=dept_temp)
    temp_dict = []
    check = 0
    if day_name not in ["Saturday", "Sunday"]:
        for i in sem_rout:
            try:
                store_temp = i.daily_routine.get(day=day_name)
                store_data = store_temp.routine_cell.filter(subject__teacher=hold)
                temp_dict.append(store_data)
            except ObjectDoesNotExist:
                pass
    else:
        check = 1
    send_data_as_dict = {
        "context": hold,
        "day": day_name,
        "check": check,
        "student": student,
        "department": dept_temp,
        "id": id,
        "emp": teachers_under,
        "dept": dept,
        "semester": semester,
        "filtered_list": filtered_list,
        "temp_dict": temp_dict,
    }
    return send_data_as_dict


@login_required
def HODHomePage(request, id):
    send_data_as_dict = fetch_me_the_data(id)
    return render(request, "HODHomePage.html", send_data_as_dict)


@login_required
def TeacherForSemester(request, id, hodid):
    try:
        send_data_as_dict = fetch_me_the_data(hodid)
        semester_id = Semester.objects.get(id=id)
        subject = SemesterWiseSubject.objects.get(semester=semester_id).subject.all()
        send_data_as_dict.update({"semester_for_sub": semester_id, "subject": subject})
        if request.method == "POST":
            data = request.POST
            for i in subject:
                try:
                    temp_teacher = data.get(f"teacher_{i.id}")
                    temp_subject = data.get(f"subject_id_{i.id}")
                    subcode_db = data.get(f"sub_code_{i.id}")
                    sub_code_db = subcode_db.upper()
                    teacher_db = Teacher.objects.get(id=temp_teacher)
                    subject_db = Subject.objects.get(id=temp_subject)
                    if TeacherSemesterSubject.objects.filter(
                        semester=semester_id, teacher=teacher_db, subject=subject_db
                    ).exists():
                        pass
                    else:
                        p = TeacherSemesterSubject.objects.create(
                            semester=semester_id,
                            teacher=teacher_db,
                            subject=subject_db,
                            subject_code=sub_code_db,
                        )
                        p.save()
                except ObjectDoesNotExist as e:
                    print(f"ObjectDoesNotExist: {e}")
                    pass
                except Exception as e:
                    print(f"An error occurred: {e}")
                    pass
            return redirect(f"/teacherforsemester/{id}/{hodid}/")
    except ObjectDoesNotExist as e:
        print(f"ObjectDoesNotExist: {e}")
        send_data_as_dict.update(
            {"error_message1": "Semester or SemesterWiseSubject not found"}
        )
        return render(request, "TeacherForSemester.html", send_data_as_dict)
    except Exception as e:
        print(f"An error occurred: {e}")
        send_data_as_dict.update({"error_message": "An error occurred"})
        return render(request, "TeacherForSemester.html", send_data_as_dict)
    return render(request, "TeacherForSemester.html", send_data_as_dict)


def return_time():
    time_arr = []
    for i in range(9):
        t = time(hour=9 + i, minute=30).strftime("%H:%M")
        time_arr.append(t)
    return time_arr


def make_the_routine(routine_data, sem):
    time_arr = return_time()
    print(time_arr)
    sem_rout = SemesterRoutine.objects.create(semester=sem)
    for key in routine_data:
        daily_routine_temp = DailyRoutine.objects.create(day=key)
        k = 0
        for i in routine_data[key]:
            print(i, type(i))
            if i == "" or i.upper() == "LAB":
                k = k + 1
                continue
            else:
                sub = TeacherSemesterSubject.objects.get(subject_code=i)
                st = time_arr[k]
                et = time_arr[k + 1]
                p = RoutineCell.objects.create(start_time=st, end_time=et, subject=sub)
                p.save()
                k = k + 1
            daily_routine_temp.routine_cell.add(p)
        daily_routine_temp.save()
        sem_rout.daily_routine.add(daily_routine_temp)
    sem_rout.save()


@login_required
def Routine(request, id1, semid):
    try:
        sem = Semester.objects.get(id=semid)
        list_of_subjects = TeacherSemesterSubject.objects.filter(semester=sem)
        if request.method == "POST":
            edited_data_json = request.POST.get("edited_data")
            edited_data = json.loads(edited_data_json)
            make_the_routine(edited_data, sem)
            return redirect(f"/routine/{id1}/{semid}/")
    except Semester.DoesNotExist:
        error_message = "Semester not found."
        return render(request, "error_page.html", {"error_message": error_message})
    except TeacherSemesterSubject.DoesNotExist:
        error_message = "Teacher Semester Subject not found."
        return render(request, "error_page.html", {"error_message": error_message})
    except json.JSONDecodeError:
        error_message = "Invalid JSON data."
        return render(request, "error_page.html", {"error_message": error_message})
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render(request, "error_page.html", {"error_message": error_message})
    return render(request, "Routine.html", {"id": id1, "list": list_of_subjects})


@login_required
def Mark(request, id, semid):
    try:
        send_data_as_dict = fetch_me_the_data(id)
        sem = Semester.objects.get(id=semid)
        teacher = Teacher.objects.filter(id=id)
        if not teacher:
            raise Teacher.DoesNotExist("Teacher with the specified ID does not exist.")
        hold = teacher[0]
        dept = hold.department
        dept_temp = Department.objects.get(department=dept)
        context_student = Student.objects.filter(department=dept_temp, semester=sem)
        subject = TeacherSemesterSubject.objects.filter(semester=sem, teacher=hold)[0]
        if request.method == "POST":
            marks_json = request.POST.get("receive")
            if not marks_json:
                raise ValueError("No marks data provided in the request.")
            marks = json.loads(marks_json)
            exam_num = request.POST.get("exam_name")
            exam_name = f"CA-{exam_num}"
            for i in marks:
                student_name = Student.objects.get(id=int(i))
                number = int(marks[i])
                EachSubjectMarks.objects.create(
                    subject_name=subject,
                    exam_name=exam_name,
                    student=student_name,
                    number=number,
                )
        send_data_as_dict.update(
            {"context_student": context_student, "subject": subject}
        )
        return render(request, "Marks.html", send_data_as_dict)
    except Semester.DoesNotExist:
        send_data_as_dict.update(
            {"error_message_marks": "Specified semester does not exist."}
        )
    except Teacher.DoesNotExist as e:
        send_data_as_dict.update({"error_message_marks": f"unexpected error: {e}"})
    except Department.DoesNotExist:
        send_data_as_dict.update(
            {"error_message_marks": "Specified Department does not exist."}
        )
    except Student.DoesNotExist:
        send_data_as_dict.update({"error_message_marks": "Student does not exist."})
    except TeacherSemesterSubject.DoesNotExist:
        send_data_as_dict.update(
            {"error_message_marks": "Specified semester subject does not exist."}
        )
    except ValueError as e:
        send_data_as_dict.update({"error_message_marks": f"An unexpected error {e}"})
    except Exception as e:
        send_data_as_dict.update(
            {"error_message_marks": f"An unexpected error occurred. Error: {e}"}
        )
    return render(request, "Marks.html", send_data_as_dict)


@login_required
def TeacherVisit(request, id, hodid):
    try:
        teacher = Teacher.objects.get(id=id)
        send_data_as_dict = fetch_me_the_data(hodid)
        teacher_sem_sub = TeacherSemesterSubject.objects.filter(teacher=teacher)
        send_data_as_dict.update(
            {"teacher": teacher, "teacher_sem_sub": teacher_sem_sub}
        )
    except Teacher.DoesNotExist:
        error_message = "Teacher not found."
        send_data_as_dict.update({"error_message": error_message})
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        send_data_as_dict.update({"error_message": error_message})
    return render(request, "TeacherVisit.html", send_data_as_dict)


@login_required
def StudentVisit(request, id, hodid):
    try:
        send_data_as_dict = fetch_me_the_data(hodid)
        students = Student.objects.filter(semester__id=id)
        student_dept_details = Semester.objects.get(id=id)
        send_data_as_dict.update(
            {"students": students, "student_dept_details": student_dept_details}
        )
    except Student.DoesNotExist:
        error_message = "Students not found."
        send_data_as_dict.update({"error_message": error_message})
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        send_data_as_dict.update({"error_message": error_message})
    return render(request, "StudentVisit.html", send_data_as_dict)


@login_required
def StudentVisitProfile(request, id, hodid):
    try:
        student = Student.objects.get(id=id)
        send_data_as_dict = fetch_me_the_data(hodid)
        send_data_as_dict.update({"student": student})
    except Student.DoesNotExist:
        error_message = "Student not found."
        send_data_as_dict.update({"error_message": error_message})
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        send_data_as_dict.update({"error_message": error_message})
    return render(request, "StudentVisitProfile.html", send_data_as_dict)


@login_required
def SeeMarks(request, semid, hodid):
    try:
        send_data_as_dict = fetch_me_the_data(hodid)
        student_data = EachSubjectMarks.objects.filter(
            subject_name__semester_id=semid, subject_name__teacher_id=hodid
        )
        a = ["CA-1", "CA-2", "CA-3", "CA-4"]
        student_list = Student.objects.filter(semester_id=semid)
        exam_result_list = []

        for i in student_list:
            temp_student_data = student_data.filter(student=i)
            temp_dict = [i.name]
            for j in a:
                try:
                    exam_result = temp_student_data.get(exam_name=j)
                    temp_dict.append(exam_result.number)
                except EachSubjectMarks.DoesNotExist:
                    temp_dict.append("")
            exam_result_list.append(temp_dict)
        send_data_as_dict.update({"CA_List": a, "exam_result_list": exam_result_list})
    except Exception as e:
        send_data_as_dict["error_see_marks"] = str(e)

    return render(request, "SeeMarks.html", send_data_as_dict)


def results_when_sem_choosen(semid, sem_name):
    exam_data = EachSubjectMarks.objects.filter(
        exam_name=sem_name, subject_name__semester_id=semid
    )
    student_list = Student.objects.filter(semester_id=semid)
    subject_list = TeacherSemesterSubject.objects.filter(semester__id=semid).order_by(
        "subject_code"
    )
    send_student_result = []
    for i in student_list:
        temp_data = [i.name]
        temp_student = exam_data.filter(student=i)
        for j in subject_list:
            try:
                exam_temp_result = temp_student.get(subject_name=j)
                temp_data.append(exam_temp_result.number)
            except EachSubjectMarks.DoesNotExist:
                temp_data.append("")
            except Exception as e:
                pass
        send_student_result.append(temp_data)
    context = {
        "student_list": student_list,
        "subject_list": subject_list,
        "send_student_result": send_student_result,
        "semtemp": sem_name,
    }
    return context


def results_when_choice_yes(semid, sem_name):
    exam_data = EachSubjectMarks.objects.filter(
        exam_name=sem_name, subject_name__semester_id=semid
    )
    student_list = Student.objects.filter(semester_id=semid)

    for i in student_list:
        temp_data = exam_data.filter(student=i)
        p = CAMarks.objects.create(student=i, exam_name=sem_name)
        for j in temp_data:
            p.each_subject_marks.add(j)
        p.save()
        try:
            temp = Marks.objects.get(student=i)
            temp.ca_exam.add(p)
            temp.save()
        except:
            temp = Marks.objects.create(
                student=i,
            )
            temp.ca_exam.add(p)
            temp.save()
    return


def results_when_choice_no(semid, sem_name):
    exam_data = EachSubjectMarks.objects.filter(
        exam_name=sem_name, subject_name__semester_id=semid
    )
    for i in exam_data:
        i.delete()
    return


@login_required
def LockViewMarks(request, hodid, semid):
    send_data_as_dict = fetch_me_the_data(hodid)
    a = ["CA-1", "CA-2", "CA-3", "CA-4"]
    send_data_as_dict.update({"CA_List": a})
    if request.method == "POST":
        sem_name = request.POST.get("sem_name")
        choice = request.POST.get("choice")
        print(sem_name, choice)
        if sem_name != "none":
            context = results_when_sem_choosen(semid, sem_name)
            print(semid, sem_name)
            send_data_as_dict.update(context)
        if choice == "yes":
            results_when_choice_yes(semid, sem_name)
        if choice == "no":
            results_when_choice_no(semid, sem_name)
    return render(request, "LockViewMarks.html", send_data_as_dict)


@login_required
def StudentDailyAttendence(request, semid, hodid):
    send_data_as_dict = fetch_me_the_data(hodid)
    try:
        teacher = Teacher.objects.get(id=hodid)
        semester = Semester.objects.get(id=semid)
        student_class = Student.objects.filter(semester=semester)
    except Exception as e:
        error_message = e
    send_data_as_dict.update({"student_class": student_class})
    today_date = datetime.now().date()
    if request.method == "POST":
        try:
            attendance_list = request.POST.get("the_data_packet")
            data_list = json.loads(attendance_list)
        except json.JSONDecodeError as e:
            error_message = e
        for i in data_list:
            print(i, data_list[i])
            if data_list[i].upper() == "PRESENT":
                status = True
            else:
                status = False
            daily_attendance = DailyAttendence.objects.create(
                date=today_date, is_present=status
            )
            daily_attendance.save()
            try:
                tws = TeacherWiseAttendence.objects.get(
                    teacher=teacher, semester__id=semid
                )
                count = tws.total_count + 1
                tws.total_count = count
                tws.dailyattendence.add(daily_attendance)
                tws.save()
            except:
                tws = TeacherWiseAttendence.objects.create(
                    teacher=teacher, semester=semester, total_count=1
                )
                tws.dailyattendence.add(daily_attendance)
                tws.save()
            try:
                temp_student = Student.objects.get(id=int(i))
            except Student.DoesNotExist:
                error_message = "Student Does Not Exists"

            try:
                attendance = Attendence.objects.get(student=temp_student)
                if attendance.teacherwiseattendence.filter(
                    teacher=teacher, semester=semester
                ).exists():
                    pass
                else:
                    attendance.teacherwiseattendence.add(tws)
                    attendance.save()
            except:
                attendance = Attendence.objects.create(student=temp_student)
                attendance.teacherwiseattendence.add(tws)
                attendance.save()
    return render(request, "StudentDailyAttendence.html", send_data_as_dict)


@login_required
def StudentHomePage(request, id):
    try:
        student = Student.objects.get(id=id)
        teacher_list = TeacherSemesterSubject.objects.filter(
            semester=student.semester
        ).order_by("subject_code")
        marks = Marks.objects.get(student=student).ca_exam.all()
        exam_name = ["subject", "Subject Code", "CA-1", "CA-2", "CA-3", "CA-4"]
        paper_list = TeacherSemesterSubject.objects.filter(
            semester=student.semester
        ).order_by("subject_code")
        all_marks = EachSubjectMarks.objects.filter(student=student)
        temp_total_list = []
        for i in paper_list:
            temp_a = [i.subject.subject, i.subject_code]
            temp_hold = all_marks.filter(subject_name=i).order_by("exam_name")
            for j in temp_hold:
                temp_a.append(j.number)
            temp_total_list.append(temp_a)

        time_slot = return_time()
        time_slot_as_header = ["Subject Code"]
        for i in range(len(time_slot) - 1):
            temp_time = time_slot[i] + "-" + time_slot[i + 1]
            time_slot_as_header.append(temp_time)

        routine_whole_week = SemesterRoutine.objects.get(
            semester=student.semester
        ).daily_routine.all()
        routine = []
        for i in routine_whole_week:
            routine_day = [i.day]
            temp_for_validation = i.routine_cell.all()

            for k in time_slot[:-1]:
                try:
                    routine_day.append(
                        temp_for_validation.get(start_time=k).subject.subject_code
                    )
                except:
                    routine_day.append("")
            routine.append(routine_day)

        context = {
            "student": student,
            "teacher_list": teacher_list,
            "marks": marks,
            "exam_name": exam_name,
            "total_list": temp_total_list,
            "time_slot_as_header": time_slot_as_header,
            "routine": routine,
        }

    except Student.DoesNotExist as e:
        context.update({"student_error": f"unexpected error: {e}"})
    except Marks.DoesNotExist as e:
        context.update({"student_error_marks": f"unexpected error: {e}"})
    except SemesterRoutine.DoesNotExist as e:
        context.update({"student_error_routine": f"unexpected error: {e}"})
    return render(request, "StudentHomePage.html", context)
