from faker import Faker
import random
from datetime import date
from .models import *
fake=Faker(locale="en_IN")
photo = ["image/20220107_115505_y9GplDn.jpg","image/20220107_115505.jpg",
         "image/20220107_115519.jpg","image/20220113_095710.jpg",
         "image/20220107_115623.jpg","image/20220107_115825.jpg"]
import random

# List of random engineering subjects
# engineering_subjects = [
#     "Mathematics for Engineers",
#     "Physics and Chemistry of Materials",
#     "Engineering Drawing and Graphics",
#     "Introduction to Computer Programming",
#     "Electrical Circuits and Networks",
#     "Mechanics of Solids",
#     "Thermodynamics",
#     "Fluid Mechanics",
#     "Differential Equations",
#     "Digital Logic Design",
#     "Control Systems",
#     "Data Structures and Algorithms",
#     "Introduction to Robotics",
#     "Material Science and Engineering",
#     "Engineering Ethics and Professionalism",
#     "Environmental Science and Engineering",
#     "Numerical Methods",
#     "Optimization Techniques",
#     "Communication Systems",
#     "Engineering Economics",
#     "Industrial Engineering",
#     "Machine Learning and Artificial Intelligence",
#     "Computer Networks",
#     "Renewable Energy Systems",
#     "Human-Computer Interaction",
#     "Biomedical Engineering",
#     "VLSI Design",
#     "Database Management Systems",
#     "Operating Systems",
#     "Software Engineering Principles",
#     "Project Management for Engineers",
#     "Engineering Geology",
#     "Geotechnical Engineering",
#     "Transportation Engineering",
#     "Structural Analysis",
#     "Hydraulics and Hydrology",
#     "Engineering Mathematics",
#     "Probability and Statistics for Engineers",
#     "Introduction to Mechatronics",
#     "Nanotechnology in Engineering",
#     "Digital Signal Processing",
#     "Microprocessor Systems",
#     "Engineering Optics",
#     "Industrial Automation",
#     "Photonics and Optoelectronics",
#     "Computational Fluid Dynamics",
#     "Power Electronics",
#     "Advanced Manufacturing Processes",
#     "Renewable Energy Technologies",
#     "Cybersecurity for Engineers",
#     "Computer-Aided Design",
#     "Instrumentation and Measurement",
#     "Robotics Programming",
#     "Introduction to Artificial Neural Networks",
#     "Fuzzy Logic and Applications",
#     "Engineering Acoustics",
#     "Composite Materials",
#     "Engineering Entrepreneurship",
#     "Virtual Reality in Engineering",
#     "Introduction to Quantum Mechanics",
#     "Engineering Risk Analysis",
#     "Game Development for Engineers",
#     "Advanced Control Systems",
#     "Digital Image Processing",
#     "Internet of Things (IoT)",
#     "Ethical Hacking for Engineers",
#     "Information Theory and Coding",
#     "Renewable Energy Policy and Planning",
#     "Sustainable Engineering Practices",
#     "Quality Control and Six Sigma",
#     "Engineering and Society",
#     "Introduction to Bioinformatics",
#     "Human Factors Engineering",
#     "Introduction to Cryptography",
#     "Introduction to Smart Grids",
#     "Wireless Communication Systems",
#     "Engineering and the Environment",
#     "Engineering for Developing Communities",
#     "Introduction to Quantum Computing",
#     "Introduction to Cyber-Physical Systems",
#     "Engineering Disaster Management",
#     "Engineering and Public Policy",
#     "Introduction to Computational Biology",
#     "Engineering Leadership and Innovation",
#     "Introduction to Satellite Communication",
#     "Engineering and Globalization",
#     "Engineering and the Arts",
#     "Introduction to Space Technology",
#     "Engineering and Cultural Diversity",
#     "Introduction to Industrial Ecology",
#     "Engineering and Social Justice",
#     "Introduction to Cognitive Science",
#     "Engineering and Philosophy",
#     "Introduction to Sustainable Design",
#     "Engineering and Human Rights",
#     "Introduction to Comparative Literature"
# ]

# sub= ["Engineering Mathematics", "Physics", "Chemistry", "Basic Electrical Engineering",
#         "Communication Skills",    "Engineering Mechanics", "Environmental Studies", 
#         "Introduction to Computers", "Introduction to Civil Engineering", "Engineering Drawing",
#         "Thermodynamics", "Workshop Practice", "Circuit Theory", "Electromagnetic Fields", 
#         "Network Analysis",    "Digital Electronics", "Analog Electronics", 
#         "Electronic Devices and Circuits", "Data Structures", "Computer Organization and Architecture",
#         "Discrete Mathematics", "Digital Logic Design", "Chemical Process Calculations", 
#         "Fluid Mechanics", "Material Science",    "Aerodynamics", "Aircraft Structures", 
#         "Flight Mechanics", "Avionics", "Human Anatomy and Physiology", "Biomaterials",    
#         "Biomechanics", "Medical Imaging", "Environmental Chemistry", "Environmental Microbiology", 
#         "Water Resources Engineering",    "Engineering Economics", "Operations Research", 
#         "Quality Control", "Manufacturing Processes"]



# sub+=engineering_subjects
# sub = set(sub)

# Print the list of random engineering subjects
# print(engineering_subjects)

def get_initials(name):
    words = name.split()  
    initials = [word[0].upper() for word in words]  
    return ''.join(initials)


def subjects():
   sub= ["Engineering Mathematics", "Physics", "Chemistry", "Basic Electrical Engineering",
        "Communication Skills",    "Engineering Mechanics", "Environmental Studies", 
        "Introduction to Computers", "Introduction to Civil Engineering", "Engineering Drawing",
        "Thermodynamics", "Workshop Practice", "Circuit Theory", "Electromagnetic Fields", 
        "Network Analysis",    "Digital Electronics", "Analog Electronics", 
        "Electronic Devices and Circuits", "Data Structures", "Computer Organization and Architecture",
        "Discrete Mathematics", "Digital Logic Design", "Chemical Process Calculations", 
        "Fluid Mechanics", "Material Science",    "Aerodynamics", "Aircraft Structures", 
        "Flight Mechanics", "Avionics", "Human Anatomy and Physiology", "Biomaterials",    
        "Biomechanics", "Medical Imaging", "Environmental Chemistry", "Environmental Microbiology", 
        "Water Resources Engineering",    "Engineering Economics", "Operations Research", 
        "Quality Control", "Manufacturing Processes"]
   for i in sub:
       try:
           sub = i
           sub_code = f'{get_initials(i)}{random.randint(100,999)}'
           Subject.objects.create(
               subject = sub,
               subject_code = sub_code,
           )
       except Exception as e:
           print(e)    

def fake_teacher_data(n=60):
    for i in range(n):
        dept = Department.objects.all()[i%3]
        name = fake.name()
        gender = "male"
        date_of_birth = fake.date()
        mail = fake.email()
        phone = fake.phone_number()
        Username = name.replace(" ","")
        try:    
            user = User.objects.create(
                username = Username,   
            )
            user.set_password(Username)
            user.save()
            Teacher.objects.create(
                user = user,
                name = name,
                gender = gender,
                date_of_birth = date_of_birth,
                mail = mail,
                phone = phone,
                department = dept,
                photo = photo[i%6],       
            )    
        except Exception as e:
            print(e)    
            
            
            
            
            
def fake_student_data(n=30):
    for i in range(n):
        dept = Department.objects.all()[i%3]
        p= Semester.objects.filter(department = dept)
        sem = p[random.randint(100,100000)%(len(p))]
        name = fake.name()
        gender = "male"
        date_of_birth = fake.date()
        mail = fake.email()
        phone = fake.phone_number()
        Username = name.replace(" ","")
        try:    
            user = User.objects.create(
                username = Username,   
            )
            user.set_password(Username)
            user.save()
            Student.objects.create(
                user = user,
                name = name,
                gender = gender,
                date_of_birth = date_of_birth,
                mail = mail,
                phone = phone,
                department = dept,
                photo = photo[i%6], 
                semester = sem
            )
        except Exception as e:
            print(e)

def AddSem():
    dept = Department.objects.all()[1:]
    sem_count = Semester_Count.objects.all()
    for i in dept:
        for j in sem_count:
            Semester.objects.create(
                department = i,
                semester_count = j
            )
    
    
def teacher_student():
    # subjects()
    # fake_teacher_data(15)
    fake_student_data(72)


def delete_data():
    u = User.objects.all()
    for i in range(8,len(u)):
        u[i].delete()
        
        
def semwisesub():
    sub = Subject.objects.all()
    sem = Semester.objects.all()[2:]
    # print(sub)
    # print(sem)
    for i in sem:
        for _ in range(5):
            index = random.randint(200,24594)%(len(sub))
            SemesterWiseSubject.objects.create(
                subject = sub[index],
                semester = i
            )
            
            



# def attendance():
#     student = Student.objects.all()
#     for i in student:
#         sem = i.semester
#         att = Attendance.objects.create(
#             semester = sem,
#             )
#         att.save()
#         i.attendance = att
#         i.save()