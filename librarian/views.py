from django.shortcuts import render,redirect
from base.models import StudentAnnouncement,User
from .models import Book,BookRequest
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
def check(request):
    return request.user.user_type=="Librarian"

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
    return render(request,'libraryDashboard.html')
def add_book(request):
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
        name = request.POST["name"]
        author = request.POST["author"]
        no_of_copies = request.POST["no_of_copies"]
        description = request.POST["description"]
        fileobj = request.FILES
        book_image = fileobj["image"]
        Book.objects.create(name=name,author=author,no_of_copies=no_of_copies,description=description,book_image=book_image)
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,f'Book {name} added successfully')
        return redirect('/librarian/dashboard')
    books = Book.objects.all()
    return render(request,'addBook.html',{'books':books})


def bookrequest(request):
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
    requests = BookRequest.objects.filter(status="Pending")
    all_request = BookRequest.objects.all()
    students = User.objects.filter(user_type="Student")
    selected_student = request.GET.get('student') if request.GET.get('student') else None
    selected_student_requests = BookRequest.objects.filter(requested_by__username=selected_student,status="Accepted") if selected_student else None
    print(selected_student_requests)
    return render(request,'bookRequest.html',{"all_students":students,
                                                'book_request':requests,
                                                'all_request':all_request,
                                                'selected_student':selected_student,
                                                'selected_student_requests':selected_student_requests})

def submit_book(request):
    if request.method=="POST":
        rid = request.POST["rid"]
        BookRequest.objects.filter(id=rid).update(status="Submitted")
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Book Returned Successfully')
        return redirect('/librarian/bookrequest')
    else:
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Not Allowed')
        return redirect('/')

def accept_book_request(request,bid):
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
    obj = BookRequest.objects.get(id=bid)
    obj2 = Book.objects.get(name=obj.book.name)
    obj2.no_of_copies =obj2.no_of_copies-1
    obj.status="Accepted"
    obj2.save(force_update=True) 
    obj.save(force_update=True)
    storage = messages.get_messages(request)
    storage.used = True
    messages.info(request,f'Request Accepted Successfully')
    return redirect('/librarian/dashboard')

def reject_book_request(request,bid):
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
    obj = BookRequest.objects.get(id=bid)
    obj.status="Rejected"
    obj.save(force_update=True)
    storage = messages.get_messages(request)
    storage.used = True
    messages.info(request,f'Request Rejected Successfully')
    return redirect('/librarian/dashboard')

def alert_user(request):
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
        name = request.POST["name"]
        obj = User.objects.get(id=name)
        name,email = obj.first_name,obj.email
        message = request.POST["message"]
        msg = 'Respected '+name+',\n\n\t'+message
        send_mail("Microsoft Engage Program",msg,from_email='adityaintern11@gmail.com',recipient_list=[email])
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,f'Email Sent Successfully')
        return redirect('/librarian/dashboard')
    obj = User.objects.filter(user_type="Student")
    return render(request,'sendmail.html',{'obj':obj})
def make_announcement(request):
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
    return render(request,'libAnnouncement.html',{'announcements':announcements})

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
    obj = StudentAnnouncement.objects.get(id=id)
    obj.delete()
    storage = messages.get_messages(request)
    storage.used = True
    messages.info(request,f'Announcement Deleted Successfully')
    return redirect('/librarian/makeAnnouncement')

def delete_book(request,id):
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
    obj = Book.objects.get(id=id)
    obj.delete()
    storage = messages.get_messages(request)
    storage.used = True
    messages.info(request,f'Book Deleted Successfully')
    return redirect('/librarian/addBook')