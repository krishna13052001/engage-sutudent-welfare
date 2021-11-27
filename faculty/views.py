from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from student.models import Course,Enrollment
from base.models import User,StudentAnnouncement
from django.contrib import messages
import csv
# Create your views here.
def check(request):
    return request.user.user_type=="Faculty"

def dashboard(request):
    if not check(request):
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Invalid Request')
        return redirect('/')
    if not request.user.is_authenticated:
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Not Logged In')
        return redirect('/')
    return render(request,'facultyDashboard.html')

def faculty_courses(request):
    if not check(request):
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Invalid Request')
        return redirect('/')
    
    if not request.user.is_authenticated:
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Not Logged In')
        return redirect('/')
    course = Course.objects.filter(faculty=request.user)
    return render(request,'facCourses.html',{'course':course})

def enrollment(request):
    if not check(request):
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Invalid Request')
        return redirect('/')
    
    if not request.user.is_authenticated:
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Not Logged In')
        return redirect('/')
    if request.method=="POST":
        student = request.POST["student"]
        course = request.POST["course"]
        if Enrollment.objects.filter(student=User.objects.get(username=student),faculty=request.user,course=Course.objects.get(name=course)).exists():
            storage = messages.get_messages(request)
            storage.used = True
            messages.info(request,f'Student {student} Already Enrolled')
            print(messages.info)
            return redirect('/faculty/enrollment')
        else:
            Enrollment.objects.create(student=User.objects.get(username=student),faculty=request.user,course=Course.objects.get(name=course))
            storage = messages.get_messages(request)
            storage.used = True
            messages.info(request,f'Student {student} Enrolled Successfully')
            return redirect('/faculty/enrollment')
    course = Course.objects.filter(faculty=request.user) 
    students = User.objects.filter(user_type="Student")
    return render(request,'enrollStudents.html',{'students':students,'course':course})

def display_students(request):
    if not check(request):
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Invalid Request')
        return redirect('/')
    
    if not request.user.is_authenticated:
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Not Logged In')
        return redirect('/')
    students = Enrollment.objects.filter(faculty=request.user)
    return render(request,'displayStudents.html',{'students':students})

def download_enrolled_students(request):
    if not check(request):
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Invalid Request')
        return redirect('/')
    
    if not request.user.is_authenticated:
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Not Logged In')
        return redirect('/')
    
    students = Enrollment.objects.filter(faculty=request.user)
    response = HttpResponse(content_type='text/csv')
    filename = request.user.username+'-'+request.user.user_type+'.csv'
    response['Content-Disposition'] = 'attachment; filename="'+filename+'"'
    writer = csv.writer(response)
    writer.writerow(['Student Name','Email ID','Course Name','Attendance','Grade'])
    for item in students:
        writer.writerow([item.student.first_name,item.student.email,item.course.name,item.attendance,item.grade])
    return response

def updateGrade(request):
    if not check(request):
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Invalid Request')
        return redirect('/')
    if not request.user.is_authenticated:
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Not Logged In')
        return redirect('/')
    if request.method=="POST":
        student_name = request.POST["name"]
        course = request.POST["course"]
        grade = request.POST['grade']
        Enrollment.objects.filter(faculty=request.user,course=Course.objects.get(name=course),student=User.objects.get(user_type="Student",first_name=student_name)).update(grade=grade)
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,f'Student {student_name} Grade Updated Successfully')
        return redirect('/faculty/dashboard')
    obj = None
    fac_courses = Course.objects.filter(faculty=request.user)
    course = request.GET.get('course') if request.GET.get('course') else None
    if course is not None:
        obj = Enrollment.objects.filter(faculty=request.user,course=Course.objects.get(name=course))
    return render(request,'updateGrade.html',{'students':obj,'fac_courses':fac_courses,'course_selected':course})

def updateAttendance(request):
    if not check(request):
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Invalid Request')
        return redirect('/')
    
    if not request.user.is_authenticated:
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Not Logged In')
        return redirect('/')
    if request.method=="POST":
        print(request.POST)
        student_name = request.POST["name"]
        course = request.POST["course"]
        attendance = request.POST['attendance']
        Enrollment.objects.filter(faculty=request.user,course=Course.objects.get(name=course),student=User.objects.get(user_type="Student",first_name=student_name)).update(attendance=attendance)
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,f'Student {student_name} Attendance Updated Successfully')
        return redirect('/faculty/dashboard')
    obj = None
    fac_courses = Course.objects.filter(faculty=request.user)
    course = request.GET.get('course') if request.GET.get('course') else None
    if course is not None:
        obj = Enrollment.objects.filter(faculty=request.user,course=Course.objects.get(name=course))
    return render(request,'updateAttendance.html',{'students':obj,'fac_courses':fac_courses,'course_selected':course})
    #obj = Enrollment.objects.filter(faculty=request.user)
    #return render(request,'updateAttendance.html',{'students':obj})

def faculty_announcement(request):
    if not check(request):
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Invalid Request')
        return redirect('/')
    
    if not request.user.is_authenticated:
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Not Logged In')
        return redirect('/')
    if request.method=="POST":
        message = request.POST["message"]
        StudentAnnouncement.objects.create(message=message,announce_from=request.user)
    announcements = StudentAnnouncement.objects.filter(announce_from=request.user)
    return render(request,'facAnnouncement.html',{'announcements':announcements})

def delete_announcement(request,id):
    if not check(request):
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Invalid Request')
        return redirect('/')
    
    if not request.user.is_authenticated:
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Not Logged In')
        return redirect('/')
    announcement = StudentAnnouncement.objects.get(id=id)
    announcement.delete()
    return redirect('/faculty/facAnnouncement')

def download_enrolled_students(request):
    if not check(request):
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Invalid Request')
        return redirect('/')
    
    if not request.user.is_authenticated:
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Not Logged In')
        return redirect('/')
    
    students = Enrollment.objects.filter(faculty=request.user)
    response = HttpResponse(content_type='text/csv')
    filename = request.user.username+'-'+request.user.user_type+'.csv'
    response['Content-Disposition'] = 'attachment; filename="'+filename+'"'
    writer = csv.writer(response)
    writer.writerow(['Student Name','Email ID','Course Name','Attendance','Grade'])
    for item in students:
        writer.writerow([item.student.first_name,item.student.email,item.course.name,item.attendance,item.grade])
    return response