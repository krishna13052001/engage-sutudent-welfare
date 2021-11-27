from django.urls import path
from . import views
urlpatterns = [
    path('dashboard',views.dashboard,name="dashboard"),
    path('facCourses',views.faculty_courses,name="facCourses"),
    path('enrollment',views.enrollment,name="enrollment"),
    path('displayStudents',views.display_students,name="displayStudents"),
    path('updateGrade',views.updateGrade,name="updateGrade"),
    path('updateAttendance',views.updateAttendance,name="updateAttendance"),
    path('facAnnouncement',views.faculty_announcement,name="facAnnouncement"),
    path('deleteAnnouncement/<int:id>',views.delete_announcement,name="deleteAnnouncement"),
    path('downloadEnrollments',views.download_enrolled_students,name="downloadEnrollments"),
]
