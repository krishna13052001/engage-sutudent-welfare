from django.urls import path
from . import views
# from django.conf.urls import (handler404)
# handler404 = 'base.views.error_404_view'
urlpatterns = [
    path('dashboard',views.dashboard,name="dashboard"),
    path('enrollments',views.enrollments,name="enrollments"),
    path('studAnnouncement',views.studAnnouncement,name="studAnnouncement"),
    path('makeBookRequest',views.makeBookRequest,name="makeBookRequest"),
    path('bookRequest/delete/<int:id>',views.bookRequesteDelete,name="bookRequesteDelete"),
    path('requestService',views.requestService,name="requestService"),
]
