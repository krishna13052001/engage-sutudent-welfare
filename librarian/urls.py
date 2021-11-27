from django.urls import path
from . import views
urlpatterns = [
    path('dashboard',views.dashboard,name="dashboard"),
    path('addBook',views.add_book,name="addBook"),
    path('bookrequest',views.bookrequest,name="bookrequest"),
    path('acceptBookRequest/<str:bid>',views.accept_book_request,name="acceptBookRequest"),
    path('rejectBookRequest/<str:bid>',views.reject_book_request,name="rejectBookRequest"),
    path('alertUser',views.alert_user,name="alertUser"),
    path('deleteBook/<int:id>',views.delete_book,name="delete_book"),
    path('deleteAnnouncement/<int:id>',views.delete_announcement,name="deleteAnnouncement"),
    path('makeAnnouncement',views.make_announcement,name="makeAnnouncement"),
    path('submitBook',views.submit_book,name="submitBook"),
]
